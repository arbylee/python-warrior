from pythonwarrior import runner
import sys


def main():
    the_runner = runner.Runner([], sys.stdin, sys.stdout)
    the_runner.run()

if __name__ == "__main__":
    main()
