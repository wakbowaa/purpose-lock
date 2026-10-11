# Purpose Lock

A data steward publishes a plain-language use charter for one named recipient. The recipient fixes the operations they intend to perform. GenLayer validators then classify every operation against the immutable purpose, allowed uses, and forbidden uses.

The contract keeps roles separate, rejects replay, requires a complete ordered verdict vector, and issues GRANTED only when every requested operation is ALLOWED.

Run `python -m pytest -q` and `genvm-lint contracts/contract.py`.

Site: https://purpose-lock.pages.dev/

