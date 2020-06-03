#coding=utf-8
from lib.javalang import parse

tree=parse.parse('''import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        System.out.println("Hello World!");
        String cmd = "echo 2333  2333";
        String cmd1 = "echo 2333 && echo 2333";
        String cmd2 = "/bin/bash -c 'echo 2333 && echo 2333'";
        String[] cmd3= { "/bin/sh", "-c", "echo 2333 && echo 2333" };
        InputStream in = Runtime.getRuntime().exec(cmd).getInputStream();

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        byte[] b = new byte[1024];
        int a = -1;

        while ((a = in.read(b)) != -1) {
            baos.write(b, 0, a);
        }

        System.out.println(new String(baos.toByteArray()));

        System.out.println("hello");

    }
}
''')



print(tree)

print(dir(tree))
print("=====")
print(tree.types[0])
print(tree.imports)
# print(tree.pac)



