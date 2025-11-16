import keyword

def convert_file(input_filename, output_filename):
    # 读取输入文件内容
    with open(input_filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    converted = []
    i = 0
    n = len(content)
    
    while i < n:
        # 检查当前位置是否为字母，可能是标识符的开始
        if content[i].isalpha():
            # 提取完整的标识符（字母、数字、下划线）
            j = i
            while j < n and content[j].isalnum() or content[j] == '_':
                j += 1
            identifier = content[i:j]
            
            # 判断是否为Python保留字，不是则转为大写
            if identifier not in keyword.kwlist:
                converted.append(identifier.upper())
            else:
                converted.append(identifier)
            
            i = j  # 移动到标识符结束位置
        else:
            # 非标识符字符直接添加
            converted.append(content[i])
            i += 1
    
    # 将转换后的内容写入输出文件
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(''.join(converted))

if __name__ == "__main__":
    input_file = "random_int.py"
    output_file = "converted_random_int.py"  # 转换后的文件
    convert_file(input_file, output_file)
    print(f"文件转换完成，结果已保存至 {output_file}")
