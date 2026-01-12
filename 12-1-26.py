def shutdown(i):
    if i == "Yes".lower():
        print("Shut down")
    elif i == "no".lower():
        print("abort shutdown.")
    else:
        print('sorry')
i=str(input("Enter whether you want to shutdown (yes / no) :"))
shutdown(i)