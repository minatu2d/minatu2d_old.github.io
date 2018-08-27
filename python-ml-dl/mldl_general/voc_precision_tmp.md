Độ chính xác trung bình nội suy

Một vài tác giả chọn một các xấp xỉ khác, được gọi là độ chính xác trung bình nội suy. Thông thường, họ gọi chúng là độ chính xác trung bình. Thay vì sử dụng P(k), hay độ chính xác khi điều chỉnh ngưỡng để lấy được ra k ảnh, độ chính xác nội suy sử dụng:


Nói cách khác, thay vì sử dụng độ chính xác trên sự quan sát sự thay đổi của k, hàm nội suy sử dụng độ chính xác cao nhất trên tất cả các giá trị recall lớn hơn k.  Công thức đầy đủ của hàm tính độ chính xác nội suy trunh bình này là:


Về mặt hình dung, ở đây là so sánh hàm tính độ chính xác nội suy trunh bình với hàm hàm xấp xỉ.

Thêm nữa, có nhiều cách khác nhau liên quan đến việc lấy mẫu ( giá trị tức thời ) tại vị trí nào khi tính toán hàm nội suy. Một số thì lấy tại 11 điểm cố định từ 0 đến 1 (bao gồm :0.1, 0.2...1.0). Cái này gọi là 11-điểm nội suy trung bình. Một số khác lại lấy tại các vị trí khi k thay đổi.

Những thứ gây khó hiểu
Một vài xuất bản quan trọng sử dụng độ chính xác nội suy làm số đo cùa họ và vẫn gọi là nó là độ chính xác trung bình. Ví dụ, PASCAL Visual Objects Challenge đã sử dụng điều này trong số đo đánh giá của họ từ 2007. Tôi không nghĩ đó là một đánh giá mạnh. Họ nói rằng: ý tưởng nội suy  trên đường cong precision/recall theo cách này sẽ giảm sự ảnh hưởng của sự lung tun trên đường cong precision/recall. Dù vậy, khi mọi người so sánh với những những người khác ở cùng độ đo trong cuộc thi thì không phải là vấn đề.
Tuy nhiên, những người khác trong chúng ta cần chú ý khi so sánh giá trị độ chính xác trung bình với những kết của xuất bản khác. Có phải chúng ta đang sử dụng độ chính xác nội suy theo kiểu VOC, trong khi họ là sử dụng độ chính xác không nội suy không?
Điều này có thể dẫn đến việc không chỉ ra được sự cải tiến một cách đứng đắn của cách mới khi so sánh với cách cũ.

Kết luận
Precision và Recall là số đo hữu dụng trong việc đánh giá hiệu năng bộ phân lớp.
Prevision và Rcall biến thiên phụ thuộc vào độ chặt của ngưỡng trong bộ phân lớp.
Có vài cách để tổng quát đường cong Precision/Recall thành một con số, con số này gọi là độ chính xác trung bình. 
Hãy chắc chắn rằng bạn đang sử dụng cùng một độ đo với xuất bản trước khi định định so sánh với chúng.

