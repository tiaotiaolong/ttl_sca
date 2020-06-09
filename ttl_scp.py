#coding=utf-8
from lib.javalang import parse
from lib.javalang.tree import *

tree=parse.parse('''

public class Main {

    public static void main(String[] args) throws IOException {
        String a="abc";
        String b = a;
        eval(b,2,4,'sss');

    }
    
}
''')

print(tree)
#函数黑名单
method_blacklist=['eval']

method_invoke_list=[]
variable_list=[]


# 解析语法树
def deal_tree(tree_node):

    #校验tree是不是列表
    if isinstance(tree_node,list):
        for item in tree_node:
            deal_tree(item)

    #tree_node为正常树的节点
    else:
        #节点类型：MethodDeclaration
        if type(tree_node) == MethodDeclaration:
            result={"method_declare":tree_node.name}

            # print(result)
            print("[+]语法树遍历到函数声明处,声明了{0}函数".format(tree_node.name))

        # 节点类型：VariableDeclarator
        if type(tree_node) == VariableDeclarator:
            # 并且是字面量赋值类型 如 a="1"
            if type(tree_node.initializer) == Literal:
                result = {"variable_literal_declare": {"variable":tree_node.name,"value":(tree_node.initializer).value}}
                variable_list.append(result)
                # print(result)
                print("[+]语法树遍历到变量声明处,变量为{0},值为{1}".format(tree_node.name,(tree_node.initializer).value))
            # 并且是引用类型 如 a=b
            if type(tree_node.initializer) == MemberReference:
                result = {"variable_reference_declare": {"variable": tree_node.name, "member": (tree_node.initializer).member}}
                variable_list.append(result)
                # print(result)
                print("[+]语法树遍历到变量声明处,变量为{0},值为{1}".format(tree_node.name, (tree_node.initializer).member))

        # 节点类型：MethodInvocation 如eval(b)
        if type(tree_node) == MethodInvocation:
            args_list=tree_node.arguments
            args=[]
            for arg in args_list:
                if type(arg) == MemberReference:
                    args.append(arg.member)
                if type(arg) == Literal:
                    args.append(arg.value)
            result={"method_call":tree_node.member,"args":args}
            method_invoke_list.append(result)
            # print(result)
            print("[+]语法树遍历到函数调用处,函数为{0},参数为{1}".format(tree_node.member,args))


        # 存在children属性
        if 'children' in dir(tree_node):
            # 对children的每个字段进行递归解析
            for item in tree_node.children:
                if item:
                    deal_tree(item)
        # 没有children的就不用处理了
        else:
            pass


deal_tree(tree)
print(method_invoke_list)
print(variable_list)
# print(isinstance(tree,tree.MethodDeclaration))
# print(type(tree)==tree.CompilationUnit)


