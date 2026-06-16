# ပစ္စည်းဈေးနှုန်းနှင့် အရေအတွက်ကို သတ်မှတ်ခြင်း
price_per_item = 1500  # ပစ္စည်းတစ်စင်းရဲ့ ဈေးနှုန်း (၁၅၀၀ ကျပ်)
quantity = 3           # ဝယ်ယူသည့် အရေအတွက် (၃ ခု)
tax_rate = 0.05        # အခွန် ၅ ရာခိုင်နှုန်း (5%)

# စုစုပေါင်း ကျသင့်ငွေကို တွက်ချက်ခြင်း
subtotal = price_per_item * quantity
tax_amount = subtotal * tax_rate
total_price = subtotal + tax_amount

# ရလဒ်ကို မျက်နှာပြင်ပေါ်တွင် ပြသခြင်း
print("--- အဝယ်စာရင်း အကျဉ်းချုပ် ---")
print(f"ပစ္စည်း စုစုပေါင်းတန်ဖိုး: {subtotal} ကျပ်")
print(f"ကျသင့်မည့် အခွန် (5%): {tax_amount} ကျပ်")
print(f"စုစုပေါင်း ပေးရမည့်ငွေ: {total_price} ကျပ်")