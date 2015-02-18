from pyramid.view import view_config
from tcga_ticker.model.enterz import TCGA
import datetime

tcga = TCGA(datetime.datetime(2000,1,1))


@view_config(route_name='default', renderer='tcga_ticker:templates/default/tcga.jinja2')
def my_view(request):
    tcgaRecord, tcgaData = tcga.records()
    # d = data.next()
    # print(d)
    # for d in tcgaData:
    #     print d['TI']
    #     print d['AU']
    #     print d.get('AB', '')[0:200]
    #     print d['PMID']
    return dict(
        tcgaRecord = tcgaRecord,
        tcgaData = tcgaData
    )
