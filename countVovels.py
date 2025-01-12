m_string = "aeiouAEIOU"


def calculate_vovels(str2):
    v_count  = 0
    for i in str2:
        if i in m_string:
            v_count+=1
    
    return v_count


def calculate_consonents(str1):
    c_count = 0
    for ch in str1:
        if ch.isalpha() and ch not in m_string:
            c_count+=1
    return c_count

try:
    str1 = input("Enter the string")
    cnt1 = calculate_vovels(str1)
    cnt2 = calculate_consonents(str1)
    print(f"The vovels are {cnt1} and consonents are {cnt2}")

except Exception as e:
    print("Enter only string.....")
    
