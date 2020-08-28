SA = 'char'
PA = 'text'
CF = 'choice'
CH = 'checkbox'
DD = 'dropdown'
FI = 'file'
DA = 'date'
TI = 'time'
DATA_TYPES = (
    (SA, 'Short Answer'),
    (PA, 'Paragraph Answer'),
    (CF, 'Choice'),
    (CH, 'Checkbox'),
    (DD, 'Dropdown'),
    (FI, 'File Upload'),
    (DA, 'Date'),
    (TI, 'Time')
)

PUB = 'published'
UNP = 'unpublished'
CLO = 'closed'
STATUS_TYPES = (
    (PUB, 'Published'),
    (UNP, 'Unpublished'),
    (CLO, 'Closed'),
)

ALL = 'all'
ADM = 'admin'
STU = 'student'
TARGET_USERS = (
    (ALL, 'All Users'),
    (ADM, 'Admin'),
    (STU, 'Student'),
)

ACC = 'accepted'
REJ = 'rejected'
WAI = 'waitlisted'
PEN = 'pending'
ACCEPTANCE_STATUSES = (
    (ACC, 'Accepted'),
    (REJ, 'Rejected'),
    (WAI, 'Waitlisted'),
    (PEN, 'Pending'),
)
