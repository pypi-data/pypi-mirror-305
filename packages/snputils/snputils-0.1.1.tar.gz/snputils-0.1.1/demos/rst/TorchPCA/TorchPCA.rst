TorchPCA
========

Fast Principal Component Analysis (PCA) implementation with PyTorch
tensors, compatible with GPU.

2022 - David Bonet

Requirements
------------

**IMPORTANT**: Not compatible with CUDA 11.3

CUDA 10.2 recommended instead: \* Conda:
``conda install pytorch cudatoolkit=10.2 -c pytorch`` \* Pip:
``pip3 install torch``

.. code:: ipython3

    import os
    import sys
    dir = os.path.abspath('../')
    if not dir in sys.path: sys.path.append(dir)
    import allel
    import torch
    import numpy as np
    from time import time

 1. Load data
-------------

.. code:: ipython3

    from snputils.snp.io.read import VCFReader

.. code:: ipython3

    reader = VCFReader("/local-scratch/mrivas/bonet/datasets/genomics/hapmap3/hapmap3.vcf")
    snpobj = reader.read()


.. parsed-literal::

    INFO:snputils.snp.io.read.vcf:Reading .vcf file: /local-scratch/mrivas/bonet/datasets/genomics/hapmap3/hapmap3.vcf
    INFO:snputils.snp.io.read.vcf:Finished reading .vcf file: /local-scratch/mrivas/bonet/datasets/genomics/hapmap3/hapmap3.vcf


.. code:: ipython3

    gt = snpobj.calldata_gt
    print(gt.shape)
    print(gt.dtype)


.. parsed-literal::

    (1035875, 1184, 2)
    int8


.. code:: ipython3

    samples = snpobj.samples
    print(samples[:5])


.. parsed-literal::

    ['2427_NA19919' '2431_NA19916' '2424_NA19835' '2469_NA20282'
     '2368_NA19703']


.. code:: ipython3

    samples_ = [s.split('_')[-1] for s in samples]
    assert len(samples_) == len(set(samples_))
    samples_




.. parsed-literal::

    ['NA19919',
     'NA19916',
     'NA19835',
     'NA20282',
     'NA19703',
     'NA19902',
     'NA19901',
     'NA19908',
     'NA19914',
     'NA20287',
     'NA20335',
     'NA19713',
     'NA19904',
     'NA19917',
     'NA19982',
     'NA20340',
     'NA20297',
     'NA19909',
     'NA19834',
     'NA20317',
     'NA19818',
     'NA20290',
     'NA20295',
     'NA20346',
     'NA19921',
     'NA20281',
     'NA20359',
     'NA20301',
     'NA20349',
     'NA20294',
     'NA20337',
     'NA20357',
     'NA19900',
     'NA20128',
     'NA20348',
     'NA20289',
     'NA20344',
     'NA20333',
     'NA20277',
     'NA20300',
     'NA19819',
     'NA20343',
     'NA19625',
     'NA20332',
     'NA19700',
     'NA20291',
     'NA20342',
     'NA20334',
     'NA20356',
     'NA20292',
     'NA20350',
     'NA20279',
     'NA20288',
     'NA20284',
     'NA19712',
     'NA20322',
     'NA19704',
     'NA19714',
     'NA19701',
     'NA20358',
     'NA20363',
     'NA20360',
     'NA20129',
     'NA19705',
     'NA19836',
     'NA20319',
     'NA20345',
     'NA20302',
     'NA19711',
     'NA20347',
     'NA19702',
     'NA20126',
     'NA20364',
     'NA20336',
     'NA19915',
     'NA19708',
     'NA20341',
     'NA19918',
     'NA19828',
     'NA19985',
     'NA20276',
     'NA20127',
     'NA19983',
     'NA06989',
     'NA11891',
     'NA11843',
     'NA12341',
     'NA12739',
     'NA10850',
     'NA06984',
     'NA12877',
     'NA12275',
     'NA06986',
     'NA12272',
     'NA10845',
     'NA10852',
     'NA07051',
     'NA12400',
     'NA12344',
     'NA12777',
     'NA12287',
     'NA10837',
     'NA12383',
     'NA12340',
     'NA12708',
     'NA12273',
     'NA11892',
     'NA12546',
     'NA12843',
     'NA12766',
     'NA12348',
     'NA12817',
     'NA10840',
     'NA06997',
     'NA11917',
     'NA12718',
     'NA12282',
     'NA11920',
     'NA12776',
     'NA12283',
     'NA07435',
     'NA12828',
     'NA07045',
     'NA07031',
     'NA12336',
     'NA07349',
     'NA12827',
     'NA12375',
     'NA12343',
     'NA12335',
     'NA12778',
     'NA12832',
     'NA11930',
     'NA12890',
     'NA07037',
     'NA07347',
     'NA12829',
     'NA12749',
     'NA11894',
     'NA12286',
     'NA10865',
     'NA10864',
     'NA10853',
     'NA11918',
     'NA12830',
     'NA12818',
     'NA10836',
     'NA11893',
     'NA11919',
     'NA12489',
     'NA12399',
     'NA12413',
     'NA10843',
     'NA12842',
     'NA12347',
     'NA07346',
     'NA12775',
     'NA07014',
     'NA12767',
     'NA12889',
     'NA12386',
     'NA06995',
     'NA12376',
     'NA12342',
     'NA12748',
     'NA11931',
     'NA12045',
     'NA12750',
     'NA11831',
     'NA12146',
     'NA11882',
     'NA07056',
     'NA12707',
     'NA12154',
     'NA12753',
     'NA11839',
     'NA10859',
     'NA12875',
     'NA07348',
     'NA12156',
     'NA12044',
     'NA11992',
     'NA11829',
     'NA12239',
     'NA12762',
     'NA12716',
     'NA12878',
     'NA10856',
     'NA12874',
     'NA12760',
     'NA06985',
     'NA12003',
     'NA10835',
     'NA07022',
     'NA12813',
     'NA10839',
     'NA07055',
     'NA12056',
     'NA10863',
     'NA12145',
     'NA12814',
     'NA10847',
     'NA12006',
     'NA12763',
     'NA07357',
     'NA12144',
     'NA10831',
     'NA07000',
     'NA11832',
     'NA06991',
     'NA11840',
     'NA12802',
     'NA12761',
     'NA10830',
     'NA10855',
     'NA06994',
     'NA11993',
     'NA11995',
     'NA12891',
     'NA12864',
     'NA12751',
     'NA10861',
     'NA12005',
     'NA12234',
     'NA07345',
     'NA07029',
     'NA12892',
     'NA12248',
     'NA10846',
     'NA12801',
     'NA12872',
     'NA12155',
     'NA06993',
     'NA11830',
     'NA10838',
     'NA12249',
     'NA12057',
     'NA12812',
     'NA11881',
     'NA11994',
     'NA12873',
     'NA12815',
     'NA12740',
     'NA12752',
     'NA12043',
     'NA12264',
     'NA10854',
     'NA12865',
     'NA18597',
     'NA18615',
     'NA18557',
     'NA18628',
     'NA18745',
     'NA18640',
     'NA18747',
     'NA18596',
     'NA18536',
     'NA18599',
     'NA18544',
     'NA18602',
     'NA18614',
     'NA18548',
     'NA18616',
     'NA18559',
     'NA18619',
     'NA18638',
     'NA18639',
     'NA18627',
     'NA18631',
     'NA18634',
     'NA18642',
     'NA18626',
     'NA18543',
     'NA18610',
     'NA18617',
     'NA18613',
     'NA18647',
     'NA18630',
     'NA18641',
     'NA18748',
     'NA18749',
     'NA18757',
     'NA18546',
     'NA18643',
     'NA18645',
     'NA18534',
     'NA18595',
     'NA18618',
     'NA18740',
     'NA18524',
     'NA18635',
     'NA18537',
     'NA18572',
     'NA18592',
     'NA18526',
     'NA18529',
     'NA18558',
     'NA18562',
     'NA18545',
     'NA18609',
     'NA18552',
     'NA18611',
     'NA18555',
     'NA18566',
     'NA18563',
     'NA18570',
     'NA18612',
     'NA18621',
     'NA18622',
     'NA18573',
     'NA18577',
     'NA18579',
     'NA18632',
     'NA18636',
     'NA18593',
     'NA18603',
     'NA18624',
     'NA18550',
     'NA18605',
     'NA18542',
     'NA18532',
     'NA18561',
     'NA18608',
     'NA18564',
     'NA18571',
     'NA18620',
     'NA18623',
     'NA18576',
     'NA18582',
     'NA18633',
     'NA18637',
     'NA18594',
     'NA17970',
     'NA17977',
     'NA17981',
     'NA17993',
     'NA18101',
     'NA18105',
     'NA18109',
     'NA18129',
     'NA18135',
     'NA18139',
     'NA18144',
     'NA18150',
     'NA18154',
     'NA18162',
     'NA17974',
     'NA17975',
     'NA17980',
     'NA17986',
     'NA17989',
     'NA17997',
     'NA18106',
     'NA18114',
     'NA18122',
     'NA18138',
     'NA18149',
     'NA17987',
     'NA17988',
     'NA17998',
     'NA18107',
     'NA18108',
     'NA18128',
     'NA18146',
     'NA18148',
     'NA18161',
     'NA18670',
     'NA18694',
     'NA18696',
     'NA17965',
     'NA17967',
     'NA17969',
     'NA17983',
     'NA18117',
     'NA18120',
     'NA18124',
     'NA18125',
     'NA18127',
     'NA18132',
     'NA18141',
     'NA18143',
     'NA18147',
     'NA18155',
     'NA18158',
     'NA18674',
     'NA17982',
     'NA17990',
     'NA18112',
     'NA18118',
     'NA18151',
     'NA18153',
     'NA18702',
     'NA18704',
     'NA17976',
     'NA17979',
     'NA18156',
     'NA18152',
     'NA18160',
     'NA18682',
     'NA18689',
     'NA18685',
     'NA17962',
     'NA17966',
     'NA17999',
     'NA17968',
     'NA17995',
     'NA17996',
     'NA18131',
     'NA18134',
     'NA18157',
     'NA18159',
     'NA17972',
     'NA18133',
     'NA18166',
     'NA18102',
     'NA18136',
     'NA18140',
     'NA20847',
     'NA20849',
     'NA20851',
     'NA20853',
     'NA20906',
     'NA20866',
     'NA21104',
     'NA20907',
     'NA20908',
     'NA21086',
     'NA21101',
     'NA21106',
     'NA21125',
     'NA21137',
     'NA21141',
     'NA21142',
     'NA20883',
     'NA20891',
     'NA20901',
     'NA21090',
     'NA21092',
     'NA21094',
     'NA21098',
     'NA21100',
     'NA21105',
     'NA21107',
     'NA21109',
     'NA20888',
     'NA20892',
     'NA20900',
     'NA20910',
     'NA21088',
     'NA21089',
     'NA21102',
     'NA20845',
     'NA20850',
     'NA20852',
     'NA20858',
     'NA20870',
     'NA20889',
     'NA20897',
     'NA20904',
     'NA20911',
     'NA21099',
     'NA21112',
     'NA21116',
     'NA20862',
     'NA21143',
     'NA21144',
     'NA20871',
     'NA20887',
     'NA20890',
     'NA20898',
     'NA20903',
     'NA20909',
     'NA21113',
     'NA21115',
     'NA21118',
     'NA21119',
     'NA21123',
     'NA21097',
     'NA20882',
     'NA20894',
     'NA20896',
     'NA20902',
     'NA20895',
     'NA20856',
     'NA20869',
     'NA20872',
     'NA20874',
     'NA20854',
     'NA20879',
     'NA21111',
     'NA20846',
     'NA20899',
     'NA21108',
     'NA20861',
     'NA20873',
     'NA20884',
     'NA21091',
     'NA20875',
     'NA20876',
     'NA20877',
     'NA21103',
     'NA20885',
     'NA21117',
     'NA20859',
     'NA20881',
     'NA18946',
     'NA18979',
     'NA19058',
     'NA18993',
     'NA19060',
     'NA19062',
     'NA18955',
     'NA18962',
     'NA18977',
     'NA18954',
     'NA19066',
     'NA19010',
     'NA19054',
     'NA19064',
     'NA19072',
     'NA19075',
     'NA19065',
     'NA19074',
     'NA19076',
     'NA19063',
     'NA19002',
     'NA19067',
     'NA19057',
     'NA19068',
     'NA19059',
     'NA19070',
     'NA19077',
     'NA19078',
     'NA19079',
     'NA19080',
     'NA19081',
     'NA19083',
     'NA19085',
     'NA19084',
     'NA19086',
     'NA18939',
     'NA19088',
     'NA19087',
     'NA19055',
     'NA18957',
     'NA18963',
     'NA19001',
     'NA19009',
     'NA19056',
     'NA18942',
     'NA18949',
     'NA18970',
     'NA18945',
     'NA18940',
     'NA18964',
     'NA18953',
     'NA18961',
     'NA18972',
     'NA18967',
     'NA18976',
     'NA18981',
     'NA18971',
     'NA18994',
     'NA18998',
     'NA19000',
     'NA18943',
     'NA18947',
     'NA18944',
     'NA18948',
     'NA18951',
     'NA18952',
     'NA18956',
     'NA18968',
     'NA18959',
     'NA18969',
     'NA18960',
     'NA18965',
     'NA18973',
     'NA18966',
     'NA18975',
     'NA18978',
     'NA18980',
     'NA18974',
     'NA18987',
     'NA18990',
     'NA18991',
     'NA18995',
     'NA18997',
     'NA19005',
     'NA18999',
     'NA19007',
     'NA19028',
     'NA19031',
     'NA19035',
     'NA19027',
     'NA19041',
     'NA19046',
     'NA19308',
     'NA19311',
     'NA19317',
     'NA19376',
     'NA19380',
     'NA19383',
     'NA19393',
     'NA19397',
     'NA19430',
     'NA19466',
     'NA19038',
     'NA19314',
     'NA19315',
     'NA19324',
     'NA19328',
     'NA19377',
     'NA19381',
     'NA19398',
     'NA19403',
     'NA19437',
     'NA19439',
     'NA19440',
     'NA19463',
     'NA19467',
     'NA19470',
     'NA19471',
     'NA19473',
     'NA19307',
     'NA19318',
     'NA19319',
     'NA19334',
     'NA19350',
     'NA19352',
     'NA19359',
     'NA19375',
     'NA19428',
     'NA19429',
     'NA19443',
     'NA19455',
     'NA19313',
     'NA19316',
     'NA19321',
     'NA19332',
     'NA19379',
     'NA19391',
     'NA19396',
     'NA19434',
     'NA19435',
     'NA19436',
     'NA19438',
     'NA19445',
     'NA19446',
     'NA19462',
     'NA19468',
     'NA19469',
     'NA19472',
     'NA19346',
     'NA19347',
     'NA19371',
     'NA19374',
     'NA19382',
     'NA19384',
     'NA19385',
     'NA19444',
     'NA19448',
     'NA19452',
     'NA19327',
     'NA19390',
     'NA19399',
     'NA19404',
     'NA19431',
     'NA19449',
     'NA19456',
     'NA19474',
     'NA19373',
     'NA19036',
     'NA19309',
     'NA19394',
     'NA19451',
     'NA19044',
     'NA19360',
     'NA19310',
     'NA19457',
     'NA19372',
     'NA19663',
     'NA19664',
     'NA19665',
     'NA19722',
     'NA19723',
     'NA19649',
     'NA19669',
     'NA19656',
     'NA19657',
     'NA19658',
     'NA19686',
     'NA19719',
     'NA19720',
     'NA19724',
     'NA19726',
     'NA19747',
     'NA19759',
     'NA19773',
     'NA19780',
     'NA19675',
     'NA19676',
     'NA19677',
     'NA19651',
     'NA19653',
     'NA19683',
     'NA19684',
     'NA19725',
     'NA19727',
     'NA19755',
     'NA19756',
     'NA19757',
     'NA19772',
     'NA19774',
     'NA19775',
     'NA19776',
     'NA19777',
     'NA19778',
     'NA19783',
     'NA19784',
     'NA19796',
     'NA19650',
     'NA19671',
     'NA19661',
     'NA19682',
     'NA19771',
     'NA19779',
     'NA19781',
     'NA19782',
     'NA19788',
     'NA19659',
     'NA19660',
     'NA19662',
     'NA19678',
     'NA19680',
     'NA19681',
     'NA19746',
     'NA19721',
     'NA19748',
     'NA19760',
     'NA19718',
     'NA19790',
     'NA19794',
     'NA19795',
     'NA19654',
     'NA19749',
     'NA19751',
     'NA19761',
     'NA19762',
     'NA19763',
     'NA19770',
     'NA19670',
     'NA19716',
     'NA19750',
     'NA19789',
     'NA19685',
     'NA19679',
     'NA19652',
     'NA21297',
     'NA21379',
     'NA21528',
     'NA21423',
     'NA21634',
     'NA21302',
     'NA21447',
     'NA21513',
     'NA21400',
     'NA21454',
     'NA21480',
     'NA21608',
     'NA21717',
     'NA21476',
     'NA21384',
     'NA21391',
     'NA21716',
     'NA21477',
     'NA21382',
     'NA21686',
     'NA21336',
     'NA21741',
     'NA21576',
     'NA21740',
     'NA21451',
     'NA21733',
     'NA21616',
     'NA21434',
     'NA21784',
     'NA21300',
     'NA21435',
     'NA21357',
     'NA21355',
     'NA21578',
     'NA21414',
     'NA21491',
     'NA21405',
     'NA21313',
     'NA21486',
     'NA21453',
     'NA21386',
     'NA21614',
     'NA21390',
     'NA21600',
     'NA21494',
     'NA21522',
     'NA21488',
     'NA21362',
     'NA21401',
     'NA21479',
     'NA21389',
     'NA21650',
     'NA21768',
     'NA21582',
     'NA21776',
     'NA21575',
     'NA21825',
     'NA21719',
     'NA21378',
     'NA21368',
     'NA21573',
     'NA21320',
     'NA21678',
     'NA21682',
     'NA21723',
     'NA21356',
     'NA21685',
     'NA21339',
     'NA21574',
     'NA21826',
     'NA21519',
     'NA21611',
     'NA21632',
     'NA21489',
     'NA21490',
     'NA21404',
     'NA21383',
     'NA21526',
     'NA21583',
     'NA21303',
     'NA21440',
     'NA21385',
     'NA21615',
     'NA21455',
     'NA21525',
     'NA21399',
     'NA21388',
     'NA21599',
     'NA21647',
     'NA21312',
     'NA21438',
     'NA21509',
     'NA21473',
     'NA21408',
     'NA21510',
     'NA21352',
     'NA21617',
     'NA21520',
     'NA21418',
     'NA21367',
     'NA21448',
     'NA21683',
     'NA21738',
     'NA21739',
     'NA21417',
     'NA21415',
     'NA21521',
     'NA21523',
     'NA21580',
     'NA21311',
     'NA21636',
     'NA21360',
     'NA21301',
     'NA21648',
     'NA21441',
     'NA21359',
     'NA21424',
     'NA21361',
     'NA21514',
     'NA21478',
     'NA21366',
     'NA21402',
     'NA21344',
     'NA21365',
     'NA21317',
     'NA21527',
     'NA21307',
     'NA21512',
     'NA21718',
     'NA21363',
     'NA21387',
     'NA21596',
     'NA21693',
     'NA21587',
     'NA21529',
     'NA21436',
     'NA21420',
     'NA21364',
     'NA21689',
     'NA21597',
     'NA21353',
     'NA21635',
     'NA21439',
     'NA21403',
     'NA21601',
     'NA21308',
     'NA21613',
     'NA21421',
     'NA21631',
     'NA21309',
     'NA21620',
     'NA21425',
     'NA21316',
     'NA21487',
     'NA21485',
     'NA21381',
     'NA21442',
     'NA21619',
     'NA21295',
     'NA21517',
     'NA21314',
     'NA21333',
     'NA21457',
     'NA21722',
     'NA21318',
     'NA21370',
     'NA21475',
     'NA21524',
     'NA21493',
     'NA21577',
     'NA21371',
     'NA20505',
     'NA20504',
     'NA20506',
     'NA20502',
     'NA20528',
     'NA20531',
     'NA20534',
     'NA20535',
     'NA20586',
     'NA20756',
     'NA20760',
     'NA20765',
     'NA20766',
     'NA20769',
     'NA20771',
     'NA20512',
     'NA20515',
     'NA20516',
     'NA20517',
     'NA20518',
     'NA20530',
     'NA20538',
     'NA20539',
     'NA20542',
     'NA20544',
     'NA20588',
     'NA20752',
     'NA20753',
     'NA20755',
     'NA20759',
     'NA20770',
     'NA20775',
     'NA20785',
     'NA20796',
     'NA20799',
     'NA20808',
     'NA20810',
     'NA20812',
     'NA20813',
     'NA20815',
     'NA20816',
     'NA20819',
     'NA20826',
     'NA20509',
     'NA20521',
     'NA20529',
     'NA20540',
     'NA20541',
     'NA20581',
     'NA20582',
     'NA20589',
     'NA20754',
     'NA20772',
     'NA20773',
     'NA20778',
     'NA20787',
     'NA20790',
     'NA20792',
     'NA20795',
     'NA20797',
     'NA20800',
     'NA20801',
     'NA20804',
     'NA20806',
     'NA20807',
     'NA20809',
     'NA20510',
     'NA20519',
     'NA20543',
     'NA20758',
     'NA20761',
     ...]



Load labels (Using PhenotypeObject)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    from snputils.phenotype.io.read import PhenotypeReader


.. parsed-literal::

    INFO:numexpr.utils:Note: NumExpr detected 56 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 8.
    INFO:numexpr.utils:NumExpr defaulting to 8 threads.


.. code:: ipython3

    phen_reader = PhenotypeReader('/local-scratch/mrivas/bonet/datasets/genomics/hapmap3/relationships_w_pops_121708.tsv')

.. code:: ipython3

    phenobj = phen_reader.read(phen_names=['population'], 
                               drop_nonphenotype_columns=True,
                               samples_column_idx=1)
    phenobj.phen_df


.. parsed-literal::

    INFO:snputils.phenotype.io.read.phenotype:Reading .tsv file: /local-scratch/mrivas/bonet/datasets/genomics/hapmap3/relationships_w_pops_121708.tsv
    INFO:snputils.phenotype.io.read.phenotype:Finished .tsv file: /local-scratch/mrivas/bonet/datasets/genomics/hapmap3/relationships_w_pops_121708.tsv




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>samples</th>
          <th>population</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>NA19625</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>1</th>
          <td>NA19702</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>2</th>
          <td>NA19700</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>3</th>
          <td>NA19701</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>4</th>
          <td>NA19705</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>1296</th>
          <td>NA19236</td>
          <td>YRI</td>
        </tr>
        <tr>
          <th>1297</th>
          <td>NA19235</td>
          <td>YRI</td>
        </tr>
        <tr>
          <th>1298</th>
          <td>NA19249</td>
          <td>YRI</td>
        </tr>
        <tr>
          <th>1299</th>
          <td>NA19248</td>
          <td>YRI</td>
        </tr>
        <tr>
          <th>1300</th>
          <td>NA19247</td>
          <td>YRI</td>
        </tr>
      </tbody>
    </table>
    <p>1301 rows × 2 columns</p>
    </div>



.. code:: ipython3

    pop_samples = phenobj.phen_df['samples'].to_list()
    print(len(pop_samples))
    print(pop_samples[:10])
    labels = phenobj.phen_df['population'].to_list()
    dict_pops = dict(zip(pop_samples,labels))


.. parsed-literal::

    1301
    ['NA19625', 'NA19702', 'NA19700', 'NA19701', 'NA19705', 'NA19703', 'NA19704', 'NA19708', 'NA19707', 'NA19711']


.. code:: ipython3

    labels = []
    for s in samples_:
        labels.append(dict_pops[s])
    labels = np.array(labels, dtype='object')
    print(np.unique(labels, return_counts=True))
    
    X = gt.astype(float)
    X = torch.from_numpy(X).permute(1,0,2)
    assert len(X) == len(labels)
    print('Original data shape: ', X.shape)
    print('Original labels shape: ', labels.shape)
    
    
    print('Combine (average) maternal and paternal strands')
    X = torch.mean(X, axis=2)
    print('Resulting shape: ', X.shape)


.. parsed-literal::

    (array(['ASW', 'CEU', 'CHB', 'CHD', 'GIH', 'JPT', 'LWK', 'MEX', 'MKK',
           'TSI', 'YRI'], dtype=object), array([ 83, 165,  84,  85,  88,  86,  90,  77, 171,  88, 167]))
    Original data shape:  torch.Size([1184, 1035875, 2])
    Original labels shape:  (1184,)
    Combine (average) maternal and paternal strands
    Resulting shape:  torch.Size([1184, 1035875])


.. code:: ipython3

    print('Use a subset of samples')
    n_subset = 500
    X = X[:n_subset, :]
    labels = labels[:n_subset]
    print('Resulting X shape: ', X.shape)
    print('Resulting labels shape: ', labels.shape)


.. parsed-literal::

    Use a subset of samples
    Resulting X shape:  torch.Size([500, 1035875])
    Resulting labels shape:  (500,)


2. Use TorchPCA
---------------

.. code:: ipython3

    # Define device
    device = 'cuda:0'
    X = X.to(device)

.. code:: ipython3

    assert X.device.type == 'cuda'

.. code:: ipython3

    from snputils.processing import TorchPCA
    pca = TorchPCA(n_components=2)

.. code:: ipython3

    start = time()
    components = pca.fit_transform(X)
    print(f'Data shape: {X.shape}, seconds running: {(time() - start):.3f}')


.. parsed-literal::

    Data shape: torch.Size([500, 1035875]), seconds running: 2.943


.. code:: ipython3

    components = components.cpu()
    components.shape




.. parsed-literal::

    torch.Size([500, 2])



 Plot components
~~~~~~~~~~~~~~~~

.. code:: ipython3

    import pandas as pd
    
    # Create dataframe
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
        "Label": labels
    })
    df.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Principal Component 1</th>
          <th>Principal Component 2</th>
          <th>Label</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>-78.273132</td>
          <td>158.006902</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>1</th>
          <td>-76.835908</td>
          <td>150.297883</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>2</th>
          <td>-71.633266</td>
          <td>130.668671</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>3</th>
          <td>-74.780976</td>
          <td>117.584241</td>
          <td>ASW</td>
        </tr>
        <tr>
          <th>4</th>
          <td>-76.803033</td>
          <td>143.232595</td>
          <td>ASW</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    import matplotlib.pyplot as plt
    import seaborn as sns

.. code:: ipython3

    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", hue="Label", linewidth=0, alpha=0.5)
    plt.grid()
    plt.legend(fontsize=20)
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on a subset of Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()



.. image:: output_25_0.png


