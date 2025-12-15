DIRECTED = False  # False: đồ thị vô hướng (undirected) | True: đồ thị có hướng (directed)

def doc_du_lieu(filename):
    """Đọc dữ liệu từ file input.txt | Read input data from input.txt"""
    with open(filename, 'r') as f:
        # Đọc số đỉnh (n) và số cạnh (m)
        # Read number of vertices (n) and edges (m)
        line1 = f.readline().split()
        n, m = int(line1[0]), int(line1[1])
        
        # Khởi tạo danh sách kề (adj)
        # Dùng n + 1 vì đỉnh thường đánh số từ 1 đến n
        # Initialize adjacency list (adj) | Use n+1 because vertices are 1..n
        adj = []
        for i in range(n + 1):
            adj.append([])
        
        for edge_index in range(m):
            u, v = map(int, f.readline().split())
            # Đồ thị vô hướng: u nối v thì v cũng nối u
            # Undirected graph: if u connects v then v connects u too
            adj[u].append(v)
            if not DIRECTED:
                adj[v].append(u)
        
        return n, m, adj

def dfs(u, adj, visited, component_nodes):
    """
    Hàm duyệt DFS để tìm tất cả các đỉnh trong cùng 1 thành phần liên thông.
    DFS traversal to collect all vertices in the same connected component.
    u: đỉnh đang xét
    u: current vertex
    component_nodes: danh sách chứa các đỉnh thuộc thành phần liên thông hiện tại
    component_nodes: list of vertices in this component
    """
    # DFS dùng stack (không dùng đệ quy) để tránh lỗi tràn ngăn xếp khi đồ thị lớn
    # Stack-based DFS (no recursion) to avoid recursion depth issues on large graphs
    stack = [u]
    visited[u] = True

    while stack:
        current = stack.pop()
        component_nodes.append(current) # Thêm đỉnh hiện tại vào danh sách thành phần
        # Add current vertex to component

        for v in adj[current]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

def giai_bai_tap(n, adj):
    visited = [False] * (n + 1)
    list_components = [] 

    #  BƯỚC 1: Tìm tất cả các thành phần liên thông 
    #  STEP 1: Find all connected components
    for i in range(1, n + 1):
        if not visited[i]:
            nodes = []
            dfs(i, adj, visited, nodes)
            list_components.append(nodes)
    #  BƯỚC 2: Xử lý 4 câu hỏi 
    #  STEP 2: Answer 4 questions
    
    # Câu 1: Đếm số thành phần liên thông
    # Q1: Count connected components
    so_tplt = len(list_components)
    print(f"1. Số thành phần liên thông: {so_tplt} (Number of connected components: {so_tplt})")
    print("   Chi tiết các thành phần: (Components details:)")
    for i, component in enumerate(list_components):
        # i+1 để đánh số thứ tự danh sách 1, 2, 3...
        # i+1 to make component index start from 1
        print(f"   - Thành phần {i+1}: {component} (Component {i+1}: {component})")
    
    # CÂU 2: Liệt kê TẤT CẢ các nhóm có số đỉnh nhiều nhất
    # Q2: List ALL components with the maximum number of vertices
    
    # B1: Tìm con số lớn nhất (max_len)
    # Step 1: Find max size (max_len)
    max_len = 0
    for comp in list_components:
        if len(comp) > max_len:
            max_len = len(comp)
            
    # B2: Lọc ra tất cả các nhóm có độ dài bằng max_len
    # Step 2: Collect all components whose size equals max_len
    cac_nhom_lon_nhat = []
    for comp in list_components:
        if len(comp) == max_len:
            cac_nhom_lon_nhat.append(comp)
            
    print(f"2. Số đỉnh nhiều nhất là: {max_len}. Các thành phần đó là: (Max size: {max_len}. Those components are:)")
    for nhom in cac_nhom_lon_nhat:
        print(f"   - {nhom}")


    # Câu 3: Có bao nhiêu TPLT có tổng số đỉnh là Chẵn 
    # Q3: How many components have an even sum of vertex labels
    count_even_sum = 0
    target_component_q4 = []

    for comp in list_components:
        total_value = sum(comp) 
        
        if total_value % 2 == 0: 
            count_even_sum += 1
            target_component_q4.append(comp)
    
    print(f"3. Số TPLT có tổng giá trị các đỉnh là chẵn: {count_even_sum} (Components with even sum: {count_even_sum})")
    print("   Các thành phần đó là: (Those components are:)")
    for comp in target_component_q4:
        print(f"   - {comp}")

    # Câu 4: Đếm số phần tử lẻ trong TPLT có tổng chẵn lớn nhất
    # Q4: Count odd-labeled vertices in the component(s) with the largest even sum
    if count_even_sum == 0:
        print("4. Không có thành phần nào có tổng chẵn. (No component has an even sum.)")
    else:
        for comp in target_component_q4:
            count_odd_nums = 0
            print(f"4. Các phần tử lẻ trong thành phần {comp} là: (Odd vertices in component {comp}:)", end=' ')
            for i in comp:
                if i % 2 != 0:
                    print(i, end=' ')
                    count_odd_nums += 1
            print(f"\nSố phần tử lẻ trong thành phần {comp} là: {count_odd_nums} (Number of odd vertices: {count_odd_nums})")
        
# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    n, m, adj = doc_du_lieu("input.txt")
    if n > 0:
        print("Đã đọc dữ liệu thành công. (Read input successfully.)")
        giai_bai_tap(n, adj)