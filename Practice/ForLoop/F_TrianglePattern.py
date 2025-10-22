# Print a triangle pattern


# rows = int(input("Enter number of rows: "))
#
# for i in range(1, rows + 1):
#     print("*" * i)



rows = int(input("Enter number of rows: "))

for i in range(0, rows, 1):
    for j in range(0, i, 1):
        print("*", end="")   # print stars on the same line
    print()  # move to the next line

# for (i = 0; i < 5; i++)
#     {
#     for (j = 0; j <= i; j++) {
# printf("*");
# }
# printf("\n");
