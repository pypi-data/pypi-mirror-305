import asyncio
from .main import main

def main_entry():
    """Entry point for the console script."""
    asyncio.run(main())

if __name__ == '__main__':
    main_entry() 