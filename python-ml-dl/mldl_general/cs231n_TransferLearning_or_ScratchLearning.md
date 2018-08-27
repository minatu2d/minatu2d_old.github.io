Khi nào và làm thế nào để fine-tune?
----

### Giới thiệu
Giả sử có một model được trained trên một tập dữ liệu sẵn có rồi, và đạt hiệu quả khá tốt trên tập dữ liệu đó rồi. 
Ví dụ, chẳng hạn:
- VGG được trained trên ImageNet. 
- InceptionV3 được trained trên COCO.

Bây giờ, khi giải quyết vấn đề phân loại ảnh cho một tập dữ liệu mới (thức ăn, quần áo, mặt nguời, etc).
Thì chúng ta nên chọn phương pháp nào?
- Tự thiết kế một mô hình mới? Cái này mình tạm gọi là Scratch Learning (hay học từ đầu).
- Sử dụng một phần của mộ hình đã cho hiệu quả phân loại tốt? Cái này đang được gọi là Transfer Learning.

Nếu sử dụng Transfer Learning chúng ta nên chọn phương pháp "transfer learning" nào cho phù hợp.
Các quyết định lựa chọn này dựa vào 2 đặc điểm rất quan trọng của tập dữ liệu mới. 
- Thứ nhất là kích thước của tập dữ liệu mới. 
- Thứ hai là tính tương tự với tập dữ liệu đã được sử dụng để trained trong mô hình ta muốn sử dụng.

Nhớ một điều rằng, các đặc trưng được mà ConvNet lấy ra thì
- Tổng quan ở các lớp truớc
- Đặc trưng ở các lớp sau.
Ví dụ với 3 lớp dữ liệu: chim sẻ, cú mèo, bồ câu khi trained thì các đặc trưng của chim sẽ được lấy ra ở các lớp truớc (giả sử: mắt, mỏ), 
còn các đặc trưng dành riêng cho mỗi loại sẽ được lấy ra ở các lớp sau (giả sử màu lông, hình dạng mặt..)

Có một vài quy tắc (dựa trên kinh nghiệm) phổ biến để định huớng cho việc quyết định chọn phương pháp nào:
#### 1. Tập dữ liệu mới là nhỏ và tương tự tập dữ liệu đã được sử dụng để trained trước đó: Linear + CNN Codes
- Dữ liệu mới nhỏ, dễ overfitting -> không nên fine-tune
- Hy vọng đặc trực lấy được từ các lớp cao (gần lớp cuối) sẽ có thể phân loại được dữ liệu mới -> sử dụng Linear cho CNN codes.
#### 2. Tập dữ liệu mới là lớn và tuơng tự tập dữ liệu đã được sử dụng để trained trước đó: Fine-tune cả network
- Có nhiều dữ liệu hơn -> có thêm tin tưởng rằng sẽ không dễ dàng bị overfitting -> fine-tune toàn bộ network.
#### 3. Tập dữ liệu mới là nhỏ và rất khác tập dữ liệu đã được sử dụng để trained trước đó: Linear, SVM + activation of earlier layer
- Dữ liệu nhỏ nên tốt nhất là linear
- Vì dữ liệu rất khác nên trained lại bộ phân loại ở lớp cuối thôi chưa hẳn đã tốt nhất.
- Có lẽ tốt hơn nếu sử dụng SVM để phân loại các activations từ các lớp sớm (lớp gần phía đầu vào)
#### 4. Tập dữ liệu mới là lớn và rất khác tập dữ liệu đã được sử dụng để trained trước đó: Train từ đầu + khởi tạo bằng pre-trained
- Bộ dữ liệu mới rất khác lại còn lớn, nên có thể thử việc trained từ đầu cả mạng luôn.
- Dù vậy, cũng có lợi nếu khởi tạo weight bằng một mô hình đã được trained sẵn
