int fibonacci(int n) {
    int a = 0, b = 1, c;

    if (n == 0)
        return 0;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return b;
}

int main() {
    int n;

    printf("Ingresa un numero: ");
    scanf("%d", &n);

    printf("Fibonacci(%d) = %d\n", n, fibonacci(n));

    return 0;
}