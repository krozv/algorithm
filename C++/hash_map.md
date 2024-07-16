# Hash Map

## unordered_map STL
- C++에서 사용할 수 있는 STL
- HashMap 자료구조로 되어 있음
- 해싱을 기반으로 데이터들을 관리해주는 자료구조
- (key, value)쌍 형태로 들어가 있어, key와 그 key에 따른 value 값을 동시에 저장
- 삽입, 삭제, 탐색 시간 복잡도 = O(1)
- `#include <unordered_map>` 헤더 필요
- 선언: `unordered_map<K, V> name;`
- K와 V에는 타입을 작성

```cpp
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int, int> m;
    return 0;
}
```
## method
### m.insert({K, V}) || m[K] = V
- hashmap에 (K, V)를 추가함
### m.erase(K)
- hashmap 데이터 중 key가 K인 데이터 쌍 제거
### m.find(K) || m[K]
- key가 존재하면 해당 iterator를 반환함
- 없다면 m.end() 값을 반환한다
- 원소는 pair 타입
```cpp
(m.find(K)) -> first // key가 K인 원소의 key를 반환
(m.find(K)) -> second // key가 K인 원소의 value를 반환
(*m.find(K)).first // key가 K인 원소의 key를 반환
(*m.find(K)).second // key가 K인 원소의 value를 반환
```