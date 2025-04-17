from gtts import gTTS
import os
import time

def text_to_speech(text, lang="vi"):
    sentences = text.split(". ")  # Tách văn bản theo dấu chấm câu
    for i, sentence in enumerate(sentences):
        if sentence.strip():  # Kiểm tra xem câu có nội dung không
            print(f"Đang đọc câu {i+1}: {sentence}")
            tts = gTTS(text=sentence, lang=lang, slow=False)
            filename = f"temp_{i}.mp3"
            tts.save(filename)
            os.system(f"start {filename}")  # Phát âm thanh
            time.sleep(2)  # Chờ một chút để đảm bảo file được phát hết

if __name__ == "__main__":
    text = """
Đại điện trầm mặc rất lâu.
Trong lòng Giang Phàm thở phào.
Đàm phán cuối cùng kết thúc.
Ít nhất có thể kéo thời gian một năm, để cho Bạch Mã tự sẽ không đối với Thiên Cơ các có địch ý.
Đến nỗi một năm sau đó đâu.
Vậy chỉ có thể đi một bước nhìn từng bước.
“Ta là tại đại lục phát hiện.”
Phổ quang trụ trì nụ cười hơi hơi ngưng kết.
Đông đảo cao tăng cùng hàng ma hộ pháp đều lộ ra im lặng chi sắc.
Ngươi chính là đại lục mà đến, người kia chắc chắn chính là tại đại lục tọa hóa.
Cái này cũng gọi manh mối?
Bất quá, cân nhắc đến đây chỉ là lần thứ nhất trao đổi manh mối, phổ quang trụ trì nhịn.
Giang Phàm chắp tay nói: “Ta hôm nay quấy rầy quý tự, cáo từ.”
“Giang thí chủ, đây là lão nạp mang theo người Kim Phật, quanh năm tại người, ẩn chứa lão nạp một tia phật vận.”
“Gặp phải không địch nổi nguy hiểm lúc, có thể đem hắn lấy ra.”
“Nhận biết vật này, bao nhiêu bán đấu giá lão nạp một bộ mặt, không quen biết, phật vận cũng biết thay ngươi tiêu tai giải nạn.”
Giang Phàm hơi kinh ngạc.
Vừa có thể ngăn cản địch nhân công kích, còn có thể hóa mục nát thành thần kỳ chữa thương.
Trước mắt vị này trụ trì Kim Phật, làm gì đều phải so với pháp ấn kim cương đầu gỗ Phật tượng mạnh a?
Phổ quang trụ trì đem Kim Phật đưa tới, nói: “Không cao hơn thực lực của ta công kích, đều có thể ngăn lại, hoặc ngươi thụ phải chết thương, hắn có thể vì ngươi bảo trụ mệnh.”
“Nhưng nhiều nhất có thể sử dụng ba lần, Giang thí chủ thận trọng sử dụng.”
Có thể bảo mệnh sao?
Giang Phàm khẽ gật đầu, nói: “Đa tạ chủ trì.”
Trong lòng đã biết rõ, vì cái gì phổ quang trụ trì muốn tiễn đưa quý trọng như vậy phòng ngự pháp bảo.
Hắn là sợ Giang Phàm bị người khô chết, không có người dời đi tiếp trời tối trụ!
Bạch Mã tự hoành hành bá đạo nhiều năm, từng đắc tội thế lực nhiều vô số kể.
“Hy vọng các ngươi Bạch Mã tự địch nhân không nên quá nhiều a!”
“Bằng không, 10 cái Kim Phật đều không đủ dùng.”
Đông đảo cao tăng mặt lộ vẻ ngượng ngùng chi sắc.
Bạch Mã tự địch nhân, là hơi nhiều.
Phổ quang trụ trì lại cười nói: “Chuyện hôm nay, chỉ cần không truyền ra ngoài, ai sẽ khó xử Giang thí chủ đâu?”
Cũng đúng.
Bọn hắn đàm phán, chỉ có Giang Phàm cùng Bạch Mã tự người biết.
Ngoại nhân chỉ coi Giang Phàm đem tiếp trời tối trụ vĩnh viễn lưu lại Bạch Mã tự, cười trên nỗi đau của người khác xem náo nhiệt đây.
Trừ phi đầu óc rút gân, mới có thể nghĩ đến tìm Giang Phàm phiền phức.
“Hảo, vậy ta cáo từ.”
“Sau một tháng Lai đại lục Yêu Tộc cảnh nội tìm ta, cho các ngươi thứ hai cái tin tức.”
Hắn quay người rời đi Bạch Mã tự.
Giang Phàm gật đầu nói: “Trong một năm, không cần lo lắng Bạch Mã tự trả thù.”
Ráng mây phi tử mắt nhìn lưu lại Bạch Mã tự tiếp trời tối trụ, có chút hiếu kỳ, Giang Phàm là như thế nào làm đến toàn thân trở ra, còn để cho Bạch Mã tự cam nguyện lưu lại tiếp trời tối trụ.
Bởi vì hắn mất đi mục tiêu.
Giang Phàm nhìn về phía nàng, lộ ra vẻ không hiểu.
Ráng mây phi tử nói: “Ngươi không phải đáp ứng linh sơ, phải bồi hắn tại tái ngoại một tháng sao?”
“Đừng để nàng một người ở đó.”
Giang Phàm trong mũi chua chua, gật đầu nói: “Hảo, trở về.”
Hai người cưỡi linh chu đi xa.
Ngay tại sắp rời xa bên bờ thời điểm, Giang Phàm hình như có chỗ xem xét nhìn về phía trên đỉnh đầu.
Bầu trời ba động lóe lên, bảy âm thượng nhân thân ảnh từ trong trạng thái ẩn thân hiện ra.
“Linh hồn cũng đạt tới một khiếu Nguyên Anh cảnh!”
Bảy âm thượng nhân mặt lộ vẻ tí ti kinh ngạc: “Thể phách, linh hồn đều đạt đến, ngay cả sức mạnh cũng mạnh đến mức ta có chút xem không hiểu.”
Bảy âm thượng nhân kiêng kỵ mắt nhìn sau lưng xa xa Bạch Mã tự, nói: “Các ngươi cứ như vậy trở về đại lục?”
“Không đi đăng thiên cổ lộ xem sao?”
“Không đi, có phần đáng tiếc a.”
“Có người ở cuối con đường cổ, thấy được thiên cổ tuyệt học, còn có người thấy được còn cao hơn trời đan lô, thậm chí thấy được chết đi ngàn năm Tôn giả lại sống lại.”
“Chúng ta Nguyên Anh cảnh đều không kịp chờ đợi muốn đi xem xét, làm gì đường này chỉ cung cấp Kết Đan cảnh khai phóng.”
“Ngươi thực lực như thế, tất nhiên có thể nhanh cùng thế hệ một bước.”
Ân?
Nghe được thiên cổ tuyệt học cùng đan lô, Giang Phàm còn không có cảm thấy cái gì.
Chết đi Tôn giả phục sinh, để cho hắn con mắt sáng lên một cái, nhưng lại cấp tốc dập tắt.
Một bên ráng mây phi tử lại lung lay hắn cánh tay, nói:
“Giang lang, không có bắt được lấn thiên thần châu phía trước, ngươi tin tưởng độ kiếp có thể tạm dừng sao?”
“Mọi thứ mắt thấy mới là thật, không đi thử thí làm sao biết đâu?”
“Vạn nhất thật có khiến người phục sinh chi pháp, ngươi không đi, chẳng phải là bỏ lỡ?”
Nàng cũng không tin có phục sinh mà nói, nhưng tin tưởng, có mục tiêu có thể để cho Giang Phàm tỉnh lại.
Giang Phàm trước mắt một lần nữa sáng lên.
Mặc dù biết, xác suất rất lớn lại là cao hứng hụt một hồi.
Cũng mặc kệ như thế nào, hắn đều nên đi xác nhận một chút.
“Bất quá, cũng hy vọng ngươi có thể tìm tới đồ nhi ta Dư Bí Diên cùng Ngụy Triêu nhiên.”
Phổ quang trụ trì khom người đứng lặng tại trước cửa điện, nói: “Phổ quang lĩnh phật chỉ, hôm nay liền chỉ phái tăng chúng tiến đến thái thương đại châu tìm kiếm chùa cổ.”
Dừng một chút, phổ quang trụ trì lại nói: “Bồ Tát, ngài vừa rồi vì cái gì không có cùng một chỗ xóa đi Giang Phàm ký ức đâu?”
Hắn thấy, Giang Phàm chính là biết cây bồ đề quý giá, mới sư tử há mồm, đề không an phận yêu cầu.
Nếu là Bồ Tát cũng xóa bỏ trí nhớ của hắn, sự tình sẽ không trở nên bị động như vậy cùng phiền phức.
Trong đại điện trầm mặc phút chốc, mới truyền đến một tiếng từ tính tiếng nói.
Con ngươi từng chút từng chút co vào.
Bao quát Giang Phàm!
Nhưng mà, Giang Phàm ký ức vậy mà không có bị xóa bỏ!
Phổ quang trụ trì bình tĩnh rất nhiều năm tháng phật tâm, nhấc lên từng đạo gợn sóng.
Cho dù là hắn, cũng đỡ không nổi Bồ Tát xóa bỏ trí nhớ Phật pháp.
Giang Phàm lại có thể!
Hắn cuối cùng biết rõ, vì cái gì Bồ Tát sẽ đáp ứng Giang Phàm, theo giai đoạn cho đầu mối yêu cầu vô lý.
Bởi vì, Bồ Tát đối với Giang Phàm có lo lắng.
Đối phương thế nhưng là hai khiếu Nguyên Anh, tốc độ như thế đi ngang qua đại lục, đều không cần nửa ngày thời gian.
Nhưng ở thái thương đại châu, 5 ngày thời gian, mới từ bờ biển đến thái thương đại châu trung ương mà thôi.
Đi ngang qua thái thương đại châu, chẳng phải là cần mười ngày trở lên?
Bảy âm thượng nhân nói: “Nhìn cùng cái gì so?”
“Cùng các ngươi đại lục làm so sánh mà nói, đại lục là một trái bồ đào, thái thương đại châu chính là một cái dưa hấu.”
Ách!
Nói đến, hắn nghe qua rất nhiều vực ngoại nhân xưng hô bọn hắn tới chỗ vì “Đại lục”, chưa từng có tên.
Vẫn luôn là “Đại lục” “Đại lục” Xưng hô.
Duy chỉ có Địa Ngục hoang thú, đã từng nói bọn hắn địa phương là “Hòn đảo”.
“Đây không phải như trò đùa của trẻ con sao?” Giang Phàm buồn bực nói.
Bảy âm thượng nhân bật cười nói: “Các ngươi cái kia, đích xác liền kêu là đại lục.”
“Ta nghe nói, trước đây thật lâu, các ngươi đó là gọi là Linh Châu Đảo.”
“Về sau, các ngươi ở trên đảo định cư một vị người thần bí, nói Linh Châu Đảo tên quá không phóng khoáng, nàng không thích, đổi tên gọi ‘Đại Lục ’, nghe thoải mái một chút.”
Ân?
Cái này phải là bao lớn đại lão, mới có thể có bực này lực ảnh hưởng?
“Đương nhiên, đây là ta nghe nói, đó đã là ngàn năm trước chuyện, thật giả không thể khảo chứng.”
“Nhưng các ngươi hòn đảo kia, đích xác liền kêu đại lục là không sai.”
Cái này......
Tốt a.
Giang Phàm nhìn về phía trước, tầng mây thấp thoáng ở giữa, từng tầng từng tầng lơ lửng cực lớn thềm đá bậc thang, nhất cấp liền nhất cấp, chui vào Thanh Minh chỗ sâu.
Mỗi một đài thềm đá, dài ước chừng vạn trượng, giống như một tòa che khuất bầu trời cổ thành.
Toàn bộ đều lơ lửng giữa không trung.
“ lớn như vậy?” Giang Phàm cảm giác sâu sắc động dung.
Trong tưởng tượng của hắn chính là từng cái thông thường cổ lão bậc thang, lan tràn hướng lên bầu trời chỗ sâu.
Nhưng trước mắt là chuyện gì xảy ra?
Bảy âm thượng nhân trong mắt cũng lộ ra sâu đậm rung động, cùng với không cách nào tự mình thăm dò cực lớn tiếc nuối.
“Ngươi nhìn thấy bậc thang, không bằng hoàn chỉnh 1%.”
Bảy âm thượng nhân lắc đầu: “Không biết.”
“Nó là theo một hồi bao phủ thái thương đại châu mê vụ xuất hiện, khi mê vụ sau khi biến mất, chỉ còn lại đầu này dài dằng dặc thông thiên Cổ Lộ.”
Ánh mắt của hắn chớp lên nói: “Tiền bối nói có người đi lên qua?”
Bảy âm thượng nhân chần chờ phút chốc, gật đầu nói: “Ân, không tệ.”
“Là một vị Tôn giả, sau khi nàng trở lại liền hạ lệnh, đem cơ duyên lưu cho Nguyên Anh phía dưới đệ tử, cường giả không cần tham dự.”
Đó chính là Hóa Thần cảnh cấp bậc tồn tại!
Liền nàng cũng không có nhìn ra hung hiểm, vấn đề cũng không lớn.
Theo hai người trò chuyện, bọn hắn đi tới tầng thứ nhất bậc thang phía trước.
Nơi đây đứng lơ lửng giữa không trung lấy nhiều Nguyên Anh cảnh cường giả, tất cả đều là các đại Thần Tông đại giáo Nguyên Anh cấp tồn tại.
Nhìn thấy bảy âm thượng nhân mang theo hai cái trẻ tuổi một nam một nữ tới, không khỏi kinh ngạc.
“Bảy âm, ngươi như thế nào mới đến?”
“Đăng thiên Cổ Lộ bảy ngày phía trước lại bắt đầu, bây giờ còn tiễn đưa đệ tử đi lên quá muộn a?”
“Có thể mấy vị kia pháp ấn kim cương độ hóa trên danh sách, đã đến phía trên nhất.”
Đi tới một vị nhìn xem hết sức trẻ tuổi thanh sắc áo dài, khuôn mặt hơi có vẻ lạnh lùng thanh niên trước mặt.
Chung quanh những người còn lại nhìn về phía trẻ tuổi trần kính thượng nhân lúc, cũng đều toát ra một tia kính ý.
Trần kính thượng nhân không chỉ có là một vị tuổi quá trẻ tứ khiếu Nguyên Anh, là uy danh hiển hách đại cường giả, càng là chân ngôn Tôn giả dưới trướng đệ tử!
Trần kính thượng nhân trong tay nâng một bản danh sách, hắn mắt nhìn bảy âm thượng nhân, lại lật lật tay bên trong danh sách, nói:
“Đệ tử của ngươi Dư Bí Diên cùng Ngụy Triêu nhiên, không phải lên đi sao?”
“Hai cái vị này là?”
Bảy âm thượng nhân danh ngạch đã dùng hết rồi.
Bảy âm thượng nhân cười xòa nói: “Hai cái vị này là vãn bối của ta.”
“Cũng nghĩ tới đăng thiên Cổ Lộ nhìn một chút, có thể hay không thỉnh trần kính thượng nhân tạo thuận lợi?”
“Ngươi tới chậm.”
“Sư tôn ta hôm qua còn tới qua một chuyến, gõ qua ta, thật sự là không còn dám tùy tiện thả người lên rồi.”
Bảy âm thượng nhân mặt lộ vẻ lúng túng.
Hắn sở dĩ dám đánh cam đoan tiễn đưa Giang Phàm bọn người đi lên, chính là cùng trần kính thượng nhân có chút giao tình.
Lại cho chút chỗ tốt, vấn đề liền không lớn.
Ai ngờ, tiểu tử này phía trước tham quá quá mức, rước lấy chân ngôn Tôn giả quở mắng.
Để cho hắn không còn dám ném loạn người.
Cái này coi như phiền toái.
Hắn lúng túng nhìn về phía Giang Phàm, đem bọn hắn xa xôi ngàn dặm mang tới, kết quả không thể lên đi.
Giang Phàm nghĩ nghĩ, lấy ra Bạch Tâm lệnh bài, nói: “Vị tiền bối này, có thể hay không tạo thuận lợi?”
Nhìn thấy này lệnh bài.
Trần kính thượng nhân hơi hơi kinh ngạc: “Ngươi là Bạch Tâm giám Thiên Vệ?”
“Người kia là ngươi?”
Giang Phàm nói: “Chính là vãn bối Giang Phàm.”
Trần kính thượng nhân chậm rãi gật đầu: “Tốt a, nếu là Bạch Tâm người, phóng ngươi đi lên, tin tưởng sư tôn cũng sẽ không nói cái gì.”
A?
Nghe Bạch Tâm rất có mặt mũi a, Tôn giả đều không thể nào bài xích hắn.
Giang Phàm ôm quyền nói: “Cảm tạ tiền bối.”
Hai người tới bậc thang phía trước.
Trần kính thượng nhân mang theo một chút do dự, hỏi: “Ngươi đã Thiên Cơ các đệ tử, nhưng biết Cửu tông?”
Ân?
Giang Phàm nao nao, không biết trước mắt trần kính thượng nhân, vì cái gì hỏi cái này, nói:
Giang Phàm nói: “Thanh Vân tông.”
Trần kính thượng nhân ánh mắt bỗng nhiên run rẩy.
Vừa có sâu đậm kinh ngạc, cũng có một phần lấp lóe rồi biến mất vui sướng, tựa hồ muốn hỏi cái gì.
Nhưng lời đến khóe miệng, lại thu về, phất tay một cái nói: “Đi thôi.”
Gật gật đầu, hắn cùng với ráng mây phi tử dắt tay bước lên bậc thang.
Bảy âm thượng nhân nghe được Giang Phàm đến từ Thanh Vân tông lúc, cũng rất là kinh ngạc, nói:
“Nếu biết ta từng là hắn đồng môn, mặt dạn mày dày hướng ta cầu cơ duyên, ta nên làm thế nào cho phải?”
“Hắn trở về đại lục, tại Thiên Cơ các làm phó các chủ cũng rất tốt.”

"""
    
    text_to_speech(text)
