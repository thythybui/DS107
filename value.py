def cmp(item):
    return item[1]  # Sắp xếp theo giá trị (value), ưu tiên giá trị lớn hơn

def solve(weight_bag, items_list):
    # Sắp xếp items_list theo value giảm dần
    items_list.sort(key=lambda: items_list[1], reverse=True)

    total_value = 0
    items_chosen = []
    for i, weight, value in items_list:
        if weight_bag >= weight:
            weight_bag -= weight
            total_value += value
            items_chosen.append(i)  # Lưu lại chỉ số của item đã chọn
        else:
            break

    print("Total value in the bag:", total_value)
    items_chosen.sort()  # Sắp xếp chỉ số của items đã chọn
    print("Items chosen:", items_chosen)

def input_items():
    item_number = int(input("Enter the number of items: "))
    weight_bag = int(input("Enter the weight of the bag: "))
    items_list = []
    
    for i in range(item_number):
        values = input().split()
        weight = int(values[0])
        value = int(values[1])
        items_list.append((i+1, weight, value))

    return weight_bag, items_list

def main():
    weight_bag, items_list = input_items()
    solve(weight_bag, items_list)

if __name__ == "__main__":
    main()