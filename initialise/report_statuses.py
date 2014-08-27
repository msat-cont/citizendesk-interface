from main import Init, init_collection

report_statuses = [{
        'name': 'new',
        'phrasing': 'This item has been received.',
}, {
        'name': 'assigned',
        'phrasing': 'This item has been assigned for verification.',
}, {
        'name': 'dismissed',
        'phrasing': 'This item has been dismissed as irrelevant.',
}, {
        'name': 'false',
        'phrasing': 'This item has been found false.',
}, {
        'name': 'verified',
        'phrasing': 'This item has been verified.',
}]

for status in report_statuses:
    status['phrasing_original'] = status['phrasing']

init_report_statuses = Init('report_status', report_statuses)

if __name__ == "__main__": init_collection(init_report_statuses)
