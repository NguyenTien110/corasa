# Corasa - the project II semester 20192

## 🌍 Tổng quan

Để phục vụ mục đích môn Đồ án II tại Trường Đại học Bách khoa Hà Nội, tôi có sử dụng Framework Rasa tạo ra 1 sản phẩm Chatbot: Corasa - kết nối với facebook messenger. 

Nhiệm vụ của Bot là đưa ra các lời khuyên, số liệu liên quan đến dịch COVID-19 mà người dùng muốn.

## 👷‍ Cài đặt

Để cài đặt Framework Rasa, hãy clone repo này về và chạy:

```
cd corasa
pip install -r requirements.txt
pip install -e .
```

Việc này để cài đặt Bot và tất cả những thứ nó cần.

Chú ý: nên dùng [python 3.6](https://www.python.org/downloads/release/python-360/) hoặc [3.7](https://www.python.org/downloads/release/python-370/).

## 🤖 To run Sara:

Đầu tiên hãy chạy lệnh sau:
```bash
rasa run actions
```

Sau đó hãy chạy lệnh `rasa train` để train model (có thể dùng tùy chọn `--fixed-model-name=corasa` để đặt tên cho model có tên là 'corasa'; nếu muốn train nhanh hơn hãy chạy thêm: `--augmentation 0`).


## 👩‍💻 Tổng quan các phần chính trong Corasa

`data/stories.md` - Gồm các kịch bản có thể sẽ có.

`data/nlu.md` - File chứa các dữ liệu để phần NLU thực hiện giai đoạn training

`actions.py` - Chứa code điều chỉnh cuộc trò chuyện.

`domain.yml` - Khai báo các intents, actions, entities(thực thể), câu trả lời cho các intents có thể có.

`config.yml` - File cấu hình cho NLU và các tất cả policy cho Bot.

## 😉 Một số command line khác

`rasa init` - Tạo 1 project mới với các file data, config, domain mặc định.

`rasa test` - Kiểm tra mô hình Rasa được đào tạo bằng cách sử dụng dữ liệu và kịch bản NLU thử nghiệm của bạn.

`rasa data split nlu` - Thực hiện phân chia dữ liệu NLU của bạn theo tỷ lệ phần trăm được chỉ định.

`rasa data convert nlu` - Chuyển đổi data NLU training giữa các định dạng.

`rasa -h` - Hiển thị các command

`rasa shell` - Chat với chatbot mình vừa tạo ra.

`rasa visualize` - Mô hình hóa các trường hợp của cuộc trò chuyện.

## ⚫️ Tài liệu tham khảo:

- Các [câu hỏi thường gặp](https://www.who.int/news-room/q-a-detail/q-a-coronaviruses) lấy từ trang chủ Tổ chức Y tế thế giới WHO.

- Luồng làm việc và lưu lại dữ liệu [tại đây](https://viblo.asia/p/tao-chatbot-tren-chatwork-tu-dong-giai-dap-thong-tin-ve-dich-covid-2020-924lJq9XZPM).

- Framework [Rasa](https://rasa.com).

- Framework [Requests](https://realpython.com/python-requests/).

- [Bot](https://github.com/RasaHQ/rasa-demo/) demo của rasa.

## 🎁 Dữ liệu lấy từ nguồn internet:

Trong project này tôi có lấy dữ liệu chi tiết của [Việt Nam](https://corona.kompa.ai/)
và thêm vào đó là tham khảo nhật ký các tình trạng COVID-19 [toàn thế giới](https://github.com/CSSEGISandData/COVID-19).
