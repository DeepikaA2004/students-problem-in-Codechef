def min_unable_to_participate(G, B):
    max_teams = min(G, B // 2)
    return B - max_teams

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    t = int(input().strip())

    # Process each test case
    for _ in range(t):
        G, B = map(int, input().strip().split())
        result = min_unable_to_participate(G, B)
        print(result)

if __name__ == "__main__":
    main()
