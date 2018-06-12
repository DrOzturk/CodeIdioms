class Hello{
  static void main(String[] args){
    println("Hello World");
    //Dynamic types
    def name = 8;
    name = "Ozgur";

    println("Hello ${name}.")
    //div defaults to float
    println(8/3)
    //int div
    println(8.intdiv(3));

    //for other operations, int is default
    println(8.2 + 1.1);
    //use methods for float
    println(8.2.plus(1.1));
    println(8.2.minus(1.1));
    println(8.2.multiply(1.1));
  }
}
