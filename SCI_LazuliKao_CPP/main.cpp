#include <iostream>
#include <vector>

class AutoPart {
public:
  AutoPart(std::string name, std::string code, std::string type, int count)
      : name(name), code(code), type(type), count(count){};
  std::string name, code, type;
  int count;

private:
};
int main() {
  std::cout << "输入数量：";
  int count;
  std::cin >> count;
  std::cout << std::endl;
  std::cout << "逐个输入单件" << std::endl;
  std::vector<AutoPart> items = std::vector<AutoPart>();
  for (int i = 1; i <= count; i++) {
    std::cout << i << " / " << count << std::endl;
    std::string name, code, type;
    int count;
    std::cout << "输入名称：";
    std::cin >> name;
    std::cout << "输入编号：";
    std::cin >> code;
    std::cout << "输入类型：";
    std::cin >> type;
    std::cout << "输入数量：";
    std::cin >> count;
    AutoPart part(name, code, type, count);
    items.push_back(part);
  }
  std::cout << "名称\t编号\t类型\t数量" << std::endl;
  for (auto &part : items) {
    std::cout << part.name << "\t" << part.code << "\t" << part.type << "\t"
              << part.count << std::endl;
  }
  std::string queryCode;
  while (true) {
    std::cout << "输入编号以查询：";
    std::cin >> queryCode;
    std::cout << "名称\t编号\t类型\t数量" << std::endl;
    int findCount = 0;
    for (auto &part : items) {
      if (part.code == queryCode) {
        ++findCount;
        std::cout << part.name << "\t" << part.code << "\t" << part.type << "\t"
                  << part.count << std::endl;
      }
    }
    if (findCount) {
      std::cout << "累计查询到" << findCount << "项" << std::endl;
    } else {
      std::cout << "无" << std::endl;
    }
  }
}