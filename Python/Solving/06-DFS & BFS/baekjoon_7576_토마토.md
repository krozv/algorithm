# [Baekjoon] 7576. 토마토
익은 토마토의 상하좌우에 위치한 토마토는 다음 날 익게 됨

토마토가 며칠이 지나면 다 익게 되는가? 최소 일수 구하시오

1: 익은 토마토

0: 익지 않은 토마토

-1: 토마토 없는 칸

## Data Structure

- 그래프
eeeeee
## Algorithm

- BFS

## How to solve
### Constraint
1. 시간 복잡도

    - 1초: 1,000,000,000번
    - 최대 input = 1,000 * 1,000
    - 단순 bfs 활용하여도 시간 초과 안날듯
   
2. 공간 복잡도

### Method

익은 토마토를 기준으로 bfs -> 상하좌우 익은 토마토로 교체

visited이 없으면 완료 후 토마토 상태 파악


### Review