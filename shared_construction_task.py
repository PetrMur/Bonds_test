def count_shares():
    total_shares = int(input())
    amount = 0
    shares = []
    for _ in range(total_shares):
        share = int(input())
        amount += share
        shares.append(share)

    for share in shares:
        print(f"{share / amount:.{3}f}")


count_shares()
