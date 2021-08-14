import math


def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료
    gong_ga_mul_11 = (10 * orderAmount + taxFreeAmount - 10 * serviceFee)
    gwa_sae_mul_11 = gong_ga_mul_11 - taxFreeAmount * 11

    VAT_mul_110 = gwa_sae_mul_11

    if 10 * gwa_sae_mul_11 + VAT_mul_110 - 110 * taxFreeAmount == 110:
        return 0
    else:
        if VAT_mul_110 % 110 == 0:
            return VAT_mul_110 // 110
        return math.ceil(VAT_mul_110 / 110)


if __name__ == "__main__":
    print(solution(120, 0, 20))
