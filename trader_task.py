from typing import Any
from functools import lru_cache


BASE_BOND_PRICE = 1000
BASE_COUPON = 1
FINAL_DAY = 30


def get_lots(trading_days: str, max_lots_in_day: str) -> list[dict[str, Any]]:
    lots = []
    bond_data = None
    number = 0
    day, bond_name, bond_cost, count = [None] * 4

    for i in range(1, int(trading_days)+1):
        for j in range(int(max_lots_in_day)):
            if bond_data is None:
                bond_data_new = input()
                bond_data = bond_data_new
                if bond_data_new == "":
                    break
                day, bond_name, bond_cost, count = bond_data.split()
            if int(day) != i:
                break
            coupon_income_summary = (int(trading_days) - i + FINAL_DAY) * BASE_COUPON * int(count)
            lot_cost = (float(bond_cost) * BASE_BOND_PRICE / 100) * int(count)
            overpayment_for_lot = lot_cost - (BASE_BOND_PRICE * int(count))
            bond_summary = {
                "data": bond_data,
                "lot_cost": lot_cost,
                "income_summary": coupon_income_summary - overpayment_for_lot,
                "number": number
            }
            if bond_summary["income_summary"] > 0:
                lots.append(bond_summary)
            number += 1
            bond_data = None

        if bond_data == "":
            break
    return lots


def find_best_bonds() -> None:
    trading_days, max_lots_in_day, cash = input().split()

    lots = get_lots(trading_days, max_lots_in_day)

    @lru_cache(maxsize=None)
    def best_income(n_bond: int, cur_cash: int) -> int:
        if n_bond == 0:
            return 0
        elif lots[n_bond - 1]["lot_cost"] > cur_cash:
            return best_income(n_bond - 1, cur_cash)
        else:
            return max(
                best_income(n_bond - 1, cur_cash),
                best_income(n_bond - 1, cur_cash - lots[n_bond - 1]["lot_cost"])
                + lots[n_bond - 1]["income_summary"])

    result = []
    cur_money = int(cash)
    for i in reversed(range(len(lots))):
        if best_income(i + 1, cur_money) > best_income(i, cur_money):
            result.append(lots[i])
            cur_money -= lots[i]["lot_cost"]

    print(sum([lot["income_summary"] for lot in result]) if result else 0)
    result.sort(key = lambda x: x["number"])
    for lot in result:
        print(lot["data"])
    print("")


find_best_bonds()
