#!/usr/bin/env python3
"""Check source validity and full generated artifacts without modifying files."""
import json
import sys
import render_lexicon as render


def main():
    try:
        domains, problems = render.parse_files()
        failures, _, stats = render.lint(domains)
        errors = problems + failures
        if not errors:
            expected = render.build_json(domains, stats)
            actual = json.loads(render.OUT_JSON.read_text(encoding='utf-8'))
            if actual != expected:
                errors.append('assets/terms.json 与源不一致（包括英文、状态、备注和模型资料），请重新生成。')
            if render.OUT_MD.read_text(encoding='utf-8') != render.build_md(domains, stats):
                errors.append('references/07-term-library.md 与源不一致，请重新生成。')
    except (OSError, ValueError, render.Problem) as exc:
        errors = [str(exc)]
    for error in errors:
        print('FAIL:', error)
    if errors:
        return 1
    print(f"PASS: {stats['terms']} 条，源与两份产物逐字段一致。")
    return 0


if __name__ == '__main__':
    sys.exit(main())
