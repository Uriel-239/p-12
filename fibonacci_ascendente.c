long long fibonacci(int n) {
    if (n < 0) return -1; 
    if (n == 0) return 0;
    if (n == 1) return 1;

    long long a = 0, b = 1, c;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

void serie_fibonacci(int n) {
    long long a = 0, b = 1, c;

    for (int i = 0; i <= n; i++) {
        if (i == 0) {
            printf("%lld", a);
        } else if (i == 1) {
            printf(", %lld", b);
        } else {
            c = a + b;
            printf(", %lld", c);
            a = b;
            b = c;
        }
    }
    printf("\n");
}

int main() {
    int n = 10;

    printf("F(%d) = %lld\n", n, fibonacci(n));
    
    printf("Serie de Fibonacci hasta F(%d):\n", n);
    serie_fibonacci(n);

    printf("\nPruebas:\n");
    for (int i = 0; i <= 10; i++) {
        printf("F(%d) = %lld\n", i, fibonacci(i));
    }

    return 0;
}