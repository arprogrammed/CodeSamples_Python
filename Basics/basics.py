def hwc(inte):
    if isinstance(inte, int) > 25:
        return "Hot"
    elif inte >= 15 and inte <= 25:
        return "Warm"
    else:
        return "Cold"
        
inte = float(input('Enter Temp:'))
print(hwc(inte))

