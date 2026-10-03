#!/usr/bin/env python3
"""兼容旧命令；词库源已迁入 lexicon/，不再接受外部源路径。"""
from render_lexicon import main
if __name__ == "__main__":
    raise SystemExit(main())
