

#✅ الهدف من الفلتر

#تحويل أي رابط موجود داخل نص (مثل: https://example.com) إلى عنصر HTML <a> حتى يكون قابل للنقر داخل صفحة HTML.






from django import template
import re

register = template.Library()

@register.filter
def linkify(text):
    if not text:
        return ''
    
    # نمط Regex يطابق أي رابط يبدأ بـ http أو https
    url_pattern = re.compile(r'(https?://[^\s]+)')
    
    # استبدال الروابط بوسم <a>
    linked_text = url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)
    
    return linked_text



# #3. استخدام الفلتر داخل القالب (template)

# داخل ملف HTML:

# {% load filters %}

# <p>{{ some_text|linkify|safe }}</p>

🔐 ملاحظة مهمة:





---

# ✨ مثال عملي

# النص داخل المتغير:

# some_text = "تابعنا على https://example.com لمزيد من التفاصيل."

# النتيجة في HTML:

# <p>تابعنا على <a href="https://example.com" target="_blank">https://example.com</a> لمزيد من التفاصيل.</p>


---

