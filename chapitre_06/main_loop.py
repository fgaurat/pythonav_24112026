
def main():
    to_find = 50
    
    for i in range(10):
        print(i)
        if i == to_find:
            break
    else:
        print("non trouvée")

if __name__=='__main__':
    main()
