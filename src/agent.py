from planner import create_plan
from executor import execute
from publisher import publish


def run():

    print("=" * 50)
    print("Market Intelligence Agent")
    print("=" * 50)

    plan = create_plan()

    execute(plan)

    publish()

    print("\nAgent completed successfully.\n")


if __name__ == "__main__":
    run()
