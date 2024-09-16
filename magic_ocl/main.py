from dataclasses import dataclass
from io import StringIO
from token import ENDMARKER, NEWLINE, OP
from tokenize import TokenInfo, generate_tokens, untokenize
from typing import Iterable
from pyecoreocl.compiler import dummy_compiler


@dataclass
class OCLExpression:
    start: tuple[int, int]
    tokens: list[TokenInfo]
    end: tuple[int, int] = (-1, -1)

    def as_string(self):
        return untokenize(
            adjust_position(token, line=1, offset=-self.start[1])
            for token in self.tokens
        )

    def compile(self, debug=False):
        ocl_code = self.as_string()
        python_code = dummy_compiler(ocl_code)
        if debug:
            print("TRACE:")
            print(" * Compiles", ocl_code)
            print(" *  as      ", python_code)
        tokens = generate_tokens(StringIO(python_code).readline)
        line, offset = self.start
        for t in tokens:
            token = adjust_position(t, line=line, offset=offset)
            if token.type == NEWLINE or token.type == ENDMARKER:
                self.end = token.end
                return
            yield token


def adjust_position(token, line=None, offset=0):
    new_start = (line if line else token.start[0], token.start[1] + offset)
    new_end = (line if line else token.end[0], token.end[1] + offset)
    return TokenInfo(
        type=token.type,
        string=token.string,
        start=new_start,
        end=new_end,
        line=token.line,
    )


def ocl2python(tokens: Iterable[TokenInfo]):
    current = None
    state = "end"
    for token in tokens:
        match token, state:
            case TokenInfo(type=OP, string="!") as t, "end":
                state = "start"
                current = OCLExpression(start=t.start, tokens=[])
            case TokenInfo(type=OP, string="!") as t, "start":
                state = "end"
                yield from current.compile(debug=False)
            case tok, "start":
                assert current
                current.tokens.append(tok)
            case tok, _:
                token = tok
                if current and current.start[0] == tok.start[0]:
                    ocl_offset = current.end[1]

                    if ocl_offset > tok.start[1]:
                        token = adjust_position(tok, offset=ocl_offset - tok.start[1])
                        current.end = token.end
                yield token


def preprocess(data: str):
    fff = ocl2python(generate_tokens(StringIO(data).readline))
    return f"""
import itertools
import pyecoreocl.runtime as ocl
{untokenize(ocl2python(generate_tokens(StringIO(data).readline)))}
"""
