#include<iostream>
#include<string>
#include<limits>
#include<vector>
#include<algorithm>
struct fixedtask {
    std::string task;
    int from;
    int to;
};
struct flexibletask {
    std::string task;
    int hours;
    int difficulty;

};
std::vector<fixedtask> fixed_task;
std::vector<flexibletask> flexible_task;
int slot{1};
int sum{0};
void fix_task(){

    int c;
    int i{1};

    while (i!=0){std::cout<<"tell fixed task"<<"\n";
        fixedtask temp;
        std::getline(std::cin,temp.task);

        std::cout<<"tell time for fixed task"<<"\n";
        std::cout<<"from"<<"\n";
        std::cin>>temp.from;
        std::cout<<"to"<<"\n";
        std::cin>>temp.to;

        std::cout<<"to add more fixed task enter 1 or to switch to flexible task enter 0"<<"\n";
        std::cin>>c;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        i=c;


    }

}

void flex_task(){
    int i{1};
    int c;

    ;
    while (i!=0) {flexibletask temp;
        std::cout<<"enter task"<<"\n";
        std::getline(std::cin,temp.task);
        std::cout<<"number of hours"<<"\n";
        std::cin>>temp.hours;

        std::cout<<"enter difficulty 1-10"<<"\n";
        std::cin>>temp.difficulty;

        std::cout<<"enter 1 or 0 "<<"\n";
        std::cin>>c;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        i=c;
    }
}
void test(){
    std:: cout<<"enter your preferred time for difficult task"<<"\n";
    std::cout<<"enter 1 morning or 0 for evening "<<"\n";
    std::cin>>slot;

    for (const auto& task : fixed_task) {
        sum+=(task.to-task.from);
    }
    for (const auto& task : flexible_task) {
        sum+=(task.hours);
    }

    if (sum>24){std::cout<<"numbers of hours of task is greater than number of days"<<"\n";}

}
struct schedule {
    std::string task;
    int hours;
    int from;
    int to;
};

bool cmp(const fixedtask& a, const fixedtask& b ) {
    return a.to>b.to;
}
std::vector<schedule> schedule;
void optimize() {
    std::ranges::sort(fixed_task.begin(), fixed_task.end(), cmp);
    for (int i{0}; i<fixed_task.size(); ++i) {
        int between{fixed_task[i].to-fixed_task[i].from};
        for (int j{0}; j<flexible_task.size(); ++j) {}
    }
    }
        //optimize time taken


int main(){
    fix_task();
    flex_task();
    test();
    return 0;
}
