# Graph - Connected Components (Vietnamese + English)

## Đề bài (Tiếng Việt)
Cho 1 đồ thị không có trọng số (vô hướng hoặc có hướng).

1. Đếm số thành phần liên thông.
2. Thành phần liên thông nào có số đỉnh nhiều nhất.
3. Giả sử tên đỉnh là các số nguyên, hỏi có bao nhiêu thành phần liên thông có tổng giá trị các đỉnh là chẵn.
4. Đếm số phần tử lẻ trong thành phần có tổng chẵn lớn nhất.

## Problem Statement (English)
Given an unweighted graph (undirected or directed).

1. Count the number of connected components.
2. Find which connected component(s) have the largest number of vertices.
3. Assume vertex labels are integers. How many components have an even sum of vertex labels?
4. Count the odd-labeled vertices in the component(s) with the largest even sum.

---

## Input format (Định dạng input)
File: `input.txt`

- Dòng 1: `n m` (số đỉnh, số cạnh) | Line 1: `n m` (number of vertices, number of edges)
- `m` dòng tiếp theo: mỗi dòng `u v` là một cạnh | Next `m` lines: each line `u v` is an edge

Ghi chú | Note:
- Code hiện tại mặc định **vô hướng** (undirected). Bạn có thể chuyển sang **có hướng** bằng cách đổi `DIRECTED = True` trong `main.py`.

## Output (Kết quả in ra)
Chương trình in ra 4 phần tương ứng với 4 câu hỏi, và mỗi dòng đều có cả tiếng Việt và tiếng Anh.

---

## Run (Cách chạy)
```powershell
cd "e:\Data\HUST\CTDL&GT\CK\Graph"
python main.py
```

---

## Example (Ví dụ)
### Input (`input.txt`)
```text
8 6
1 2
2 3
4 5
6 7
7 8
6 8
```

### Output (mẫu / sample)
(Thứ tự các đỉnh trong từng thành phần có thể khác nhau do thứ tự duyệt DFS.)

```text
Đã đọc dữ liệu thành công. (Read input successfully.)
1. Số thành phần liên thông: 3 (Number of connected components: 3)
   Chi tiết các thành phần: (Components details:)
   - Thành phần 1: [1, 2, 3] (Component 1: [1, 2, 3])
   - Thành phần 2: [4, 5] (Component 2: [4, 5])
   - Thành phần 3: [6, 8, 7] (Component 3: [6, 8, 7])
2. Số đỉnh nhiều nhất là: 3. Các thành phần đó là: (Max size: 3. Those components are:)
   - [1, 2, 3]
   - [6, 8, 7]
3. Số TPLT có tổng giá trị các đỉnh là chẵn: 1 (Components with even sum: 1)
   Các thành phần đó là: (Those components are:)
   - [1, 2, 3]
4. Các phần tử lẻ trong thành phần [1, 2, 3] là: (Odd vertices in component [1, 2, 3]:) 1 3
Số phần tử lẻ trong thành phần [1, 2, 3] là: 2 (Number of odd vertices: 2)
```
