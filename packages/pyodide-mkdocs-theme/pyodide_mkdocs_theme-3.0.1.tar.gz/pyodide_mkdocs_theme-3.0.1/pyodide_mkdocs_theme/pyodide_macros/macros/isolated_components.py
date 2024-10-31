"""
pyodide-mkdocs-theme
Copyleft GNU GPLv3 🄯 2024 Frédéric Zinelli

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.
If not, see <https://www.gnu.org/licenses/>.
"""
# pylint: disable=unused-argument


import re
from functools import wraps
from typing import Optional

from mkdocs.exceptions import BuildError


from ..tools_and_constants import MACROS_WITH_INDENTS, HtmlClass
from ..parsing import build_code_fence
from .. import html_builder as Html
from ..plugin.maestro_macros import MaestroMacros
from .ide_manager import IdeManager





def script(
    env: MaestroMacros,
    nom: str,
    *,
    lang: str='python',
    stop= None,
) -> str:
    """
    Renvoie le script dans une balise bloc avec langage spécifié

    - lang: le nom du lexer pour la coloration syntaxique
    - nom: le chemin du script relativement au .md d'appel
    - stop: si ce motif est rencontré, il n'est pas affichée, ni la suite.
    """
    target = env.get_sibling_of_current_page(nom, tail='.py')
    _,content,public_tests = env.get_hdr_and_public_contents_from(target)

    # Split again if another token is provided
    if stop is not None:
        # rebuild "original" if another token is provided
        if public_tests:
            content = f"{ content }{ env.lang.tests.msg }{ public_tests }"
        content = re.split(stop, content)[0]

    indent = env.get_macro_indent()
    out = build_code_fence(content, indent, lang=lang)
    return out



def py(env:MaestroMacros):
    """
    Macro python rapide, pour insérer le contenu d'un fichier python. Les parties HDR sont
    automatiquement supprimées, de même que les tests publics. Si un argument @stop est
    fourni, ce dot être une chaîne de caractère compatible avec re.split, SANS matching groups.
    Tout contenu après ce token sera ignoré (token compris) et "strippé".

    ATTENTION: Ne marche pas sur les exercices avec tous les codes python dans le même fichier.
    """
    MACROS_WITH_INDENTS.add('py')

    @wraps(py)
    def wrapped(py_name: str, stop=None, **_) -> str:
        return script(env, py_name, stop=stop)
    return wrapped





def figure(env:MaestroMacros):
    """
    Macro pour insérer une <div> qui devra contenir une figure dessinée ensuite via matplotlib,
    par exemple(ou autre!).
    """
    MACROS_WITH_INDENTS.add('figure')

    def p5_btn(kind:str, div_id:str):
        return IdeManager.cls_create_button(
            env,
            f'p5_{ kind }',
            id=f"{ kind }-btn-{ div_id }",
            extra_btn_kls='p5-btn'
        )

    @wraps(figure)
    def wrapped(
        div_id:      Optional[str] = None, #"figure1",
        *,
        div_class:   Optional[str] = None, #"py_mk_figure",
        inner_text:  Optional[str] = None, #'Votre tracé sera ici',
        admo_kind:   Optional[str] = None, #'!!!',
        admo_class:  Optional[str] = None, #'tip',
        admo_title:  Optional[str] = None, #'Votre Figure',
        p5_buttons:  Optional[str] = None, #None,
    ):
        code = Html.div(inner_text, id=div_id, kls=div_class)

        if p5_buttons:
            if p5_buttons not in ('left','right'):
                raise BuildError(f"Invalid value for `p5_buttons`: {p5_buttons!r}")

            buttons_order = 'stop','start'
            buttons = Html.div(
                ''.join( p5_btn(kind, div_id) for kind in buttons_order ),
                kls=HtmlClass.p5_btns_wrapper
            )
            wrapped = buttons+code if p5_buttons=='left' else code+buttons
            code = Html.div(wrapped, kls=HtmlClass.p5_figure_wrapper)

        if admo_kind:
            code = f"""\n
{admo_kind} {admo_class} "{admo_title}"
    {code}
\n"""

        out_code = env.indent_macro(code)
        return out_code

    return wrapped
