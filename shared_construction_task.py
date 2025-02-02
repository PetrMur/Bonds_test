def count_shares():
    total_shares = int(input())
    amount = 0
    shares = []
    for _ in range(total_shares):
        share = float(input())
        amount += share
        shares.append(share)

    for share in shares:
        print(f"{share / amount:.3f}")


count_shares()
