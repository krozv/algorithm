// 성적조회
#include <iostream>
#include <map>
#include <string>
#include <set>
using namespace std;

struct Student {
    int grade;
    string gender;
    int score;
};

map<int, Student> m;
map<pair<int, string>, map<int, set<int>>> infoMap;

/// *** user.cpp ***
void init() {
    m.clear();
    infoMap.clear();
}
int addScore(int id, int grade, char gender[], int score) {
	string genderString(gender);
    m[id] = {grade, genderString, score};

    // grader랑 genderString으로 이루어진 map 생성
    map<int, set<int>>& scoreMap = infoMap[make_pair(grade, genderString)];
    // score-id map 생성
    scoreMap[score].insert(id);

    // 가장 마지막 순서 return
    auto lastElementSet = scoreMap.rbegin()->second;
    return *lastElementSet.rbegin();
}
int removeScore(int id) {
	if (m.find(id) == m.end()) {
        return 0;
    }

    Student info = m[id];
    map<int, set<int>>& scoreMap = infoMap[make_pair(info.grade, info.gender)];

    scoreMap[info.score].erase(id);
    if (scoreMap[info.score].empty()) {
        scoreMap.erase(info.score);
    }
    m.erase(id);

    if (scoreMap.empty()) {
        return 0;
    }

     auto it = scoreMap.begin();
    return *(it->second.begin());
}
int get(int gradeCnt, int grade[], int genderCnt, char gender[][7], int score) {

	return 0;
}
// 메인코드 
///*** main.cpp ***
#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

extern void init();
extern int addScore(int id, int grade, char gender[], int score);
extern int removeScore(int id);
extern int get(int gradeCnt, int grade[], int genderCnt, char gender[][7], int score);

/////////////////////////////////////////////////////////////////////////

#define CMD_INIT 100
#define CMD_ADD 200
#define CMD_REMOVE 300
#define CMD_GET 400

static bool run() {
	int q;
	scanf("%d", &q);

	int id, grade, score;
	char gender[7];
	int cmd, ans, ret;
	bool okay = false;

	for (int i = 0; i < q; ++i) {
		scanf("%d", &cmd);
		switch (cmd) {
		case CMD_INIT:
			init();
			okay = true;
			break;
		case CMD_ADD:
			scanf("%d %d %s %d %d", &id, &grade, gender, &score, &ans);
			ret = addScore(id, grade, gender, score);
			if (ans != ret)
				okay = false;
			break;
		case CMD_REMOVE:
			scanf("%d %d", &id, &ans);
			ret = removeScore(id);
			if (ans != ret)
				okay = false;
			break;
		case CMD_GET: {
			int gradeCnt, genderCnt;
			int gradeArr[3];
			char genderArr[2][7];
			scanf("%d", &gradeCnt);
			if (gradeCnt == 1) {
				scanf("%d %d", &gradeArr[0], &genderCnt);
			}
			else if (gradeCnt == 2) {
				scanf("%d %d %d", &gradeArr[0], &gradeArr[1], &genderCnt);

			}
			else {
				scanf("%d %d %d %d", &gradeArr[0], &gradeArr[1], &gradeArr[2], &genderCnt);
			}
			if (genderCnt == 1) {
				scanf("%s %d %d", genderArr[0], &score, &ans);
			}
			else {
				scanf("%s %s %d %d", genderArr[0], genderArr[1], &score, &ans);
			}

			ret = get(gradeCnt, gradeArr, genderCnt, genderArr, score);
			if (ans != ret)
				okay = false;
			break;

		}

		default:
			okay = false;
			break;
		}
	}
	return okay;
}


int main() {
	setbuf(stdout, NULL);
	freopen("input.txt", "r", stdin);
	int T, MARK;
	scanf("%d %d", &T, &MARK);
		for (int tc = 1; tc <= T; tc++) {
			int score = run() ? MARK : 0;
			printf("#%d %d\n", tc, score);
		}
		return 0;
}