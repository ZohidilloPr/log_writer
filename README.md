# WriteLogger
`WriteLogger` - Bu Loglarni filega yozib borish uchun kichik packege.

## O'rnatish

Paketni o'rnatish uchun quyidagi buyruqni ishga tushiring:

```bash
pip install log-writer
```

## Foydalanish
import pathlib
from log_writer.logger import WriteLogger

# Bazaviy direktoriyani aniqlang
`BASE_DIR = pathlib.Path(__file__).parent`

# WriteLogger obyektini yaratish
`logger = WriteLogger(BASE_DIR)`

# Info log yozish
`logger.info("This is an informational message.")`

# Error log yozish
`logger.error("This is an error message.")`

# Qo'shimcha Ma'lumot
Agar qo'shimcha savollaringiz bo'lsa yoki muammolarga duch kelsangiz, quyidagi manzil orqali menga murojaat qiling:
 - **email**: zohidilloturgunov@mail.ru
 - **github**: [ZohidilloPr](https://github.com/ZohidilloPr/)
   
