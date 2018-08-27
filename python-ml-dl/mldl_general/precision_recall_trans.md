Là chim hay máy bay phụ thuộc vào mức độ điều chỉnh bộ phân loại

Đánh giá một hệ thống truy vấn (hay tìm kiếm, đặt câu hỏi, tìm kiếm) thông tin (như phần mềm tìm kiếm chẳng hạn), thường tập trung vào 2 thứ sau:

1. Mức độ thích hợp của kết quả truy vấn được. (Precision - độ chính xác)
2. Hệ thống truy vấn được nhiều kết quả chính xác không? (Recall - độ triệu hồi tạm dịch vậy )

Cho những ai không quen, tôi sẽ giả thích thế nào là Precision và Recall. Khi đã quen rồi, tôi sẽ giải thích về một vài khó hiểu trong tài liệu lúc xem xét đường cong Precision-Recall.

# Giữa Con ngỗng và máy bay

Lấy ví dụ về ngỗng và máy bay vì hình dáng khá giống nhau.

Khi truy vấn ảnh hệ thống của bạn (bằng câu hỏi, bằng từ khoá tìm kiếm, bằng ảnh mẫu về máy bay, etc), bạn sẽ muốn hệ thống lấy ra toàn bộ ảnh về máy bay thôi, không chứa bất cứ ảnh của một con ngỗng nào.

Quan trọng : Lấy ra máy bay là mục đích của hệ thống này, nó có thể trả ra máy bay hoặc không trả ra cái gì trong mỗi truy vấn.

Giả sử cho một đống ảnh mà hệ thống của bạn phải lấy chọn ra từ đó theo yêu cầu truy vấn của bạn.
Chúng ta sẽ đếm số lượng kết quả theo số 4 loại sau:
Positive hay Negative : Là thao tác hệ thống
Positive : Được hiểu là dương tính hoặc tương tự trong hệ thống khác, ở đây xin dịch là Lấy
Negative : Được hiểu là âm tính hoặc tương tự trên hệ thống khác, ở đây xin dịch là Bỏ.

True, False: Đánh giá hệ thống
True: Đúng, False : đương nhiên là sai.


*True positive* ( Lấy đúng) : số ảnh máy bay mà hệ thống lấy được ( chưa hẳn là tất cả số máy bay mà hệ thống có).

*True Negative* ( Bỏ hay éo lấy đúng) : tức là số ảnh ngỗng mà không được hệ thống lấy ra. Tuyệt vời nhất là còn nguyên bằng số ảnh ngỗng ban đầu của bộ ảnh.

*False Positive*  ( Lấy ra nhưng sai CMNR) : Số ảnh ngỗng mà hệ thống hiểu nhầm là máy bay rồi lấy ra. 

*False Negative* ( Lại đi bỏ cái ảnh đáng lẽ phải lấy, bỏ sai CMNR) : Số ảnh máy bay mà hệ thống éo lấy ra vì cho rằng nó là ngỗng.


Áp dụng những định nghĩa ở trên, chúng ta thử tìm số ảnh tương ứng với mỗi loại trong ví dụ xem sao.

Có 3 cái lấy đúng, tức là lấy được 3 cái máy bay thật. Cũng ngon đấy chứ.(True Positive)
Có 1 cái lấy ra nhưng sai CMNM. tức là lấy mie con ngỗng ra bảo là máy bay rồi. Ngu VKL. (False Positive)
Có 2 cái bỏ sai CMNR, tức là bỏ 2 cái máy bay éo lấy rồi.(False Negative)
Có 4 cái bỏ đúng, tức là 4 con ngỗn éo được lấy. (True Negative)

Nhìn vào 4 con số ở trên thì ta có thể nói hệ thống tốt hay không.
Giờ AI rồi, có lẽ ta nên gọi từ hệ thống Ngáo hay Thông minh.

Ví dụ: 
Lấy đúng nhiều là tốt, càng lấy đúng nhiều càng tốt (True Positive càng cao càng tốt)
Lấy sai ít là tốt, càng lấy sai ít càng tốt (False Positive càng thấp càng tốt.
Bỏ sai ít là tốt, càng bỏ sai ít càng tốt (False Negative càng thấp càng tốt)
Bỏ đúng nhiều là tốt, càng bỏ đúng nhiều càng tốt (True Negative càng cao càng tốt).

Nghe thì rất đơn giản phải không, những trong các hệ thống từ Ngáo lên Thông minh thì không phải bao giờ cũng rõ ràng được. Vì chúng là máy, hiện tại chúng chưa phân biệt thật sự tốt giữa một cái ảnh là máy bay với một ảnh là con ngỗng đang bay.
Đôi khi đơn giản chỉ là điều chỉnh mức một tham số (hay gọi là ngưỡng) lên cao hay xuống thấp thì kết quả của việc xem một ảnh là máy bay hay ngỗng đang bay cũng thay đổi rồi.

Precision và Recal ( Số đo độ chính xác và số đo độ triệu hồi)

Giờ chúng ta sẽ hiểu chính xác 2 khái niệm về Precision  và Recall.

Số đo độ chính xác (Precision) là tỉ lệ phần trăm số lấy đúng trên toàn bộ số lượng đã lấy ra từ hệ thống. Tổng số đã lấy sẽ bằng số lấy đúng (True Positive) và lấy sai (False Positive).

Số đo độ triệu hồi (Recall) là tỉ lệ phần trăm lấy ra đúng (số máy bay đã lấy ra) trên tổng số may bay mà hệ thống có. Số may bay hệ thống có bằng số đã lấy ra (True Positive) và số máy bay không được lấy ra (hay bị bỏ nhầm CNMR chính là False Negative).

Trong ví dụ của chúng ta ở trên, xin nhắc lại:
Lấy đúng (True Positive) : 3
Lấy sai (False Positive) : 1
Bỏ sai (False Negative) : 2
Bỏ đúng (True Negative) : 4

số đo độ chính xác (Precision) : 3 / (3 + 1) = 0.75
số đo độ triệu hồi (Recall) : 3/ (3 + 2) = 0.6

Nói bằng lời, có 75% số lượng lấy ra đúng là máy bay, có 60% số máy bay của cả hệ thống được lấy ra.

2 con số là 100% đương nhiên là lý tưởng rồi. Nhưng khó mà đạt được như thế trong cái hệ thống đang học cách chuyển từ Ngáo sang Thông minh. Và gần như 2 số đo này sẽ tăng giảm ngược nhau. Tùy vào yêu cầu mà phải điều chỉnh tham số để cân bằng 2 số đo này.

Như đã nói ở trên, việc này dựa vào thay đổi tham số( hay gọi là ngưỡng ) của tham số trong hệ thống.

Điều chỉnh ngưỡng

Phải làm gì nếu chúng ta không thấy thoả mãn (happy) với hiệu năng hiện tại. Chúng ta có thể yêu cầu hệ thống lấy ra nhiều kết quả hơn ( ví dụ điều chỉnh ngưỡng để dễ chấp nhận một ảnh là máy bay hơn).  Điều này sẽ giảm nhẹ mức độ của ngưỡng để coi một ảnh là máy bay. Chúng ta cũng có thể yêu cầu hệ thống phải cứng rắn hơn, trả về ít hơn nhưng chính xác hơn chẳng hạn. 
Trong ví dụ sau đây

Trong ví dụ sau đây, hệ thống trả về 4 lần tương ứng với một ngưỡng cụ thể nào đó ( miêu tả bằng đường kẻ màu xanh). Hệ thống sẽ trả về những ảnh mà giống máy bay hơn hoặc bằng ngưỡng đó. Ngưỡng ở đây có thể coi như độ giống đi.
Chúng ta có thể di chuyển lên xuống để có được những tập kết quả khác nhau được trả về.

Tương ứng với đó, ở mỗi vị trí của ngưỡng, ta sẽ thu được giá trị khác nhau của Precision  ( số đo độ chính xác ) và Recall (số đo độ triệu hồi). 
Cụ thể hơn, nếu chúng ta điều chỉnh ngưỡng để chỉ lấy ảnh trên cùng, ta sẽ có Precision là 100%, và Recall là 20%. Nếu chúng ta lấy điều chỉnh ngưỡng để chỉ lấy 2 anh trên cùng, Precision sẽ là 100%, và Recall đã lên đến 40% rồi. 
Bảng sau sẽ chỉ ra quan hệ giữa Precision và Recall tại các ngưỡng khác nhau.

# Đường cong Precision - Recall ( Đường cong của số đo độ chính xác và độ triệu hồi)

Một cách rất hay để miêu tả hiệu năng của một bộ phân lớp là xem xét sự thay đổi của Precision và Recall khi thay đổi ngưỡng. Một bộ phân lớp tốt (hay không Ngáo) sẽ xếp hạng các thực sự là máy bay ở phía trên của danh sách khi chọn ngưỡng. Nó cũng có khả năng lấy rất nhiều ảnh của máy bay trước có trong hệ thống. Hay nói cách khác Precision nằm ở mức cao khi Recall tăng. Một bộ phân lớp tồi ( hay Ngáo) sẽ ăn đạn ( giảm ) Precision khi có Recall cao. Thông thường, các nghiên cứu sẽ trình bày đường cong Precision-Recall để đưa ra mặt cân bằng cho bộ phân lớp của họ.

Dưới đây là một đồ thì giữa Precision và Recall.

# Số đo độ chính xác trung bình
Đánh giá trên một đường cong vẫn tương đối khó hiểu. Một con số có thể đánh giá đặc trực hiệu năng hệ thống chắc chắn sẽ dễ hiểu hơn nhiều.

