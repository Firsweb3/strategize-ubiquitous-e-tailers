public class RandomDataGenerator {
        int[] data = new int[10];
        for (int i = 0; i < 10; i++) {
    public static void main(String[] args) {

            data[i] = (int) (Math.random() * 100) + 1;
    }
        for (int item : data) {
}
            System.out.println("Random Number: " + item);
        }

        }def main():


    data = [random.randint(1, 100) for _ in range(10)]

    main()
    data = generate_random_data()
if __name__ == "__main__":
def generate_random_data():
    return data

import random
    for item in data:
        print(f"Random Number: {item}")