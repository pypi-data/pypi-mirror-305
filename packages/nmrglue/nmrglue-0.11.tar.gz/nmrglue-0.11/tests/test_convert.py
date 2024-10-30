""" Tests for the fileio.convert submodule """


import tempfile
import os
import shutil
import sys
import glob
from re import sub

# Ignore UserWarnings when converting Bruker data
import warnings
warnings.simplefilter('ignore', UserWarning)

import nmrglue as ng
from numpy.testing import assert_array_equal

from setup import DATA_DIR


if sys.version_info[0] == 2:
    _string_type = basestring
else:
    _string_type = str


# subroutines
def check_sdic(dic1, dic2, exclude=None, v=False):
    """ Check two Sparky parameter dictionaries against each other """
    if exclude is None:
        exclude = []
    # check axis dictionaries
    if 'w1' in dic1:
        check_pdic(dic1["w1"], dic2["w1"], exclude=exclude, v=v)
        exclude.append('w1')

    if 'w2' in dic1:
        check_pdic(dic1["w2"], dic2["w2"], exclude=exclude, v=v)
        exclude.append('w2')

    if 'w3' in dic1:
        check_pdic(dic1["w3"], dic2["w3"], exclude=exclude, v=v)
        exclude.append('w3')

    # check remainder
    check_pdic(dic1, dic2, exclude=exclude, v=v)


def check_dic(dic1, dic2, exclude=None, v=False):
    """ Compare two parameter dictionaries """
    if exclude is None:
        exclude = []
    e1 = [k for k in dic1.keys() if k not in dic2.keys() and k not in exclude]
    e2 = [k for k in dic2.keys() if k not in dic2.keys() and k not in exclude]

    if v:
        print(e1)
    assert len(e1) == 0
    if v:
        print(e2)
    assert len(e2) == 0

    if v:
        for k in dic1.keys():
            if k in exclude:
                continue
            if dic1[k] != dic2[k]:
                print(k, dic1[k], dic2[k])

    for k in dic1.keys():
        if k in exclude:
            continue
        assert dic1[k] == dic2[k]


def check_pdic(dic1, dic2, exclude=None, v=False):
    """ Compare two NMRPipe parameter dictionaries """
    if exclude is None:
        exclude = []
    e1 = [k for k in dic1.keys() if k not in dic2.keys() and k not in exclude]
    e2 = [k for k in dic2.keys() if k not in dic2.keys() and k not in exclude]

    if v:
        print(e1)
    assert len(e1) == 0
    if v:
        print(e2)
    assert len(e2) == 0

    if v:
        for k in dic1.keys():
            if k in exclude:
                continue
            if isinstance(dic1[k], _string_type) or isinstance(dic1[k], list):
                if dic1[k] != dic2[k]:
                    print(k, dic1[k], dic2[k])
            elif abs(dic1[k] - dic2[k]) >= 0.002:
                print(k, dic1[k], dic2[k], dic1[k] - dic2[k])

    for k in dic1.keys():
        if k in exclude:
            continue
        if isinstance(dic1[k], _string_type) or isinstance(dic1[k], list):
            assert dic1[k] == dic2[k]
        else:
            assert abs(dic1[k] - dic2[k]) <= 0.002


def check_rdic(dic1, dic2, ndim, exclude=None, v=True):
    """ Compare two RNMRTK parameter dictionaries up to dimension ndim"""
    if exclude is None:
        exclude = []

    non_list_keys = ['comment', 'format', 'ndim', 'layout']
    list_keys = ['dom', 'nacq', 'npts', 'nptype', 'cphase', 'lphase', 'quad',
                 'sf', 'sw', 'xfirst', 'xstep', 'ppm']

    # check keys which are not lists
    for k in non_list_keys:
        if k in exclude:
            continue
        if v:
            if dic1[k] != dic2[k]:
                print(k, dic1[k], dic2[k])
        assert dic1[k] == dic2[k]

    # check keys which are lists for first ndim parameters
    for k in list_keys:
        if k in exclude:
            continue
        for i in range(ndim):
            if k in ['dom', 'nptype', 'quad']:  # these are strings
                if v:
                    if dic1[k][i] != dic2[k][i]:
                        print(k, i, dic1[k][i], dic2[k][i])
                assert dic1[k][i] == dic2[k][i]
                continue

            if v:
                if abs(dic1[k][i] - dic2[k][i]) > abs(dic1[k][i] / 1000.):
                    print(k, i, dic1[k][i], dic2[k][i])
                if abs(dic1[k][i] - dic2[k][i]) > abs(dic2[k][i] / 1000.):
                    print(k, i, dic1[k][i], dic2[k][i])
            assert abs(dic1[k][i] - dic2[k][i]) <= abs(dic1[k][i] / 1000.)
            assert abs(dic1[k][i] - dic2[k][i]) <= abs(dic2[k][i] / 1000.)
    return


bad_varian_keys = ["procpar"]
bad_pipe_keys = ["FDYEAR", "FDMONTH", "FDDAY", "FDHOURS", "FDMINS", "FDSECS"]
bad_bruker_keys = ["pprog", "acqus", "acqu2s", "acqu3s"]
bad_sparky_keys = ['bsize', 'extended', 'date', 'owner']
# bad_rnmrtk_keys = ['layout', 'comment', 'p0', 'p1']
bad_rnmrtk_keys = ['nacq', 'cphase', 'lphase']

# keys which are bad because rnmrtk sets them incorrect when outputting NMRPipe
# formatted data
bad_rnmrtk2pipe_keys = [
    "FDF1LABEL", "FDF2LABEL", "FDF3LABEL", "FDF4LABEL",
    "FDF1QUADFLAG", "FDF2QUADFLAG", "FDF3QUADFLAG", "FDF4QUADFLAG",
    "FDDIMORDER1", "FDDIMORDER2", "FDDIMORDER3", "FDDIMORDER4",
    "FDF1P0", "FDF2P0", "FDF3P0", "FDF4P0",
    "FDF1P1", "FDF2P1", "FDF3P1", "FDF4P1",
    "FDF1SIZE", "FDF2SIZE", "FDF3SIZE", "FDF4SIZE",
    "FDF1TDSIZE", "FDF2TDSIZE", "FDF3TDSIZE", "FDF4TDSIZE",
    "FDF1APOD", "FDF2APOD", "FDF3APOD", "FDF4APOD",
    "FDF1CENTER", "FDF2CENTER", "FDF3CENTER", "FDF4CENTER",
    "FDF1UNITS", "FDF2UNITS", "FDF3UNITS", "FDF4UNITS",
    "FDDIMORDER", "FDREALSIZE", "FDFLTFORMAT", "FD2DVIRGIN", "FDPIPEFLAG",
    "FDCOMMENT", "FD2DPHASE", "FDFILECOUNT"]


# tests


def test_agilent_1d():
    """ 1D time agilent, pipe <-> agilent, pipe """
    # prepare agilent converter
    vdic, vdata = ng.varian.read(os.path.join(DATA_DIR, "agilent_1d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "agilent_1d",
                                            "test.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # agilent -> agilent
    cdic, cdata = vC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)

    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rdic, rdata = ng.varian.read(td)
    assert_array_equal(vdata, rdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)

    # agilent -> pipe
    cdic, cdata = vC.to_pipe()
    assert_array_equal(pdata, cdata)
    # check_pdic(pdic, cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    # check_pdic(pdic, cdic)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata)
    check_pdic(pdic, cdic, bad_pipe_keys)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    check_pdic(pdic, cdic, bad_pipe_keys)
    os.remove(tf)

    # pipe -> agilent
    cdic, cdata = pC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rdic, rdata = ng.varian.read(td)
    assert_array_equal(vdata, rdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_agilent_1d_rnmrtk():
    """ 1D time agilent, rnmrtk <-> rnmrtk """
    # prepare agilent converter
    vdic, vdata = ng.varian.read(os.path.join(DATA_DIR, "agilent_1d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare rnmrtk converter
    rdic, rdata = ng.rnmrtk.read(os.path.join(DATA_DIR, "rnmrtk_1d",
                                 "time_1d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic, agilent_compatible=True)

    # agilent -> rnmrtk
    cdic, cdata = vC.to_rnmrtk(agilent_compatible=True)
    assert_array_equal(rdata, cdata)
    # check_rdic(rdic, cdic, 1, bad_rnmrtk_keys)     # XXX do not check
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(cdata, rrdata)
    check_rdic(cdic, rrdic, 1)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk(agilent_compatible=True)
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 1, bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    check_rdic(rdic, rrdic, 1, bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> agilent
    cdic, cdata = rC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rrdic, rrdata = ng.varian.read(td)
    assert_array_equal(vdata, rrdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_agilent_2d():
    """ 2D time agilent, pipe <-> agilent, pipe """
    # prepare Varian converter
    vdic, vdata = ng.varian.read(os.path.join(DATA_DIR, "agilent_2d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "agilent_2d",
                                            "test.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # varian -> varian
    cdic, cdata = vC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rdic, rdata = ng.varian.read(td)
    assert_array_equal(vdata, rdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)

    # varian -> pipe
    cdic, cdata = vC.to_pipe()
    assert_array_equal(pdata, cdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata)
    check_pdic(pdic, cdic, bad_pipe_keys)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    check_pdic(pdic, cdic, bad_pipe_keys)
    os.remove(tf)

    # pipe -> varian
    cdic, cdata = pC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rdic, rdata = ng.varian.read(td)
    assert_array_equal(vdata, rdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_agilent_2d_rnmrtk():
    """ 2D time agilent, rnmrtk <-> rnmrtk """
    # prepare agilent converter
    vdic, vdata = ng.varian.read(os.path.join(DATA_DIR, "agilent_2d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare rnmrtk converter
    rdic, rdata = ng.rnmrtk.read(os.path.join(DATA_DIR, "rnmrtk_2d",
                                 "time_2d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic, agilent_compatible=True)

    # agilent -> rnmrtk
    cdic, cdata = vC.to_rnmrtk(agilent_compatible=True)
    assert_array_equal(rdata, cdata)
    # check_rdic(rdic, cdic, 2, bad_rnmrtk_keys)     # XXX do not check
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(cdata, rrdata)
    check_rdic(cdic, rrdic, 2)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk(agilent_compatible=True)
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 2, bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    check_rdic(rdic, rrdic, 2, bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> agilent
    cdic, cdata = rC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rrdic, rrdata = ng.varian.read(td)
    assert_array_equal(vdata, rrdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_agilent_3d():
    """ 3D time agilent, pipe <-> agilent, pipe """
    # prepare Agilent converter
    vdic, vdata = ng.varian.read(os.path.join(DATA_DIR, "agilent_3d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare NMRPipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "agilent_3d", "data",
                                            "test%03d.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # agilent -> agilent
    cdic, cdata = vC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rdic, rdata = ng.varian.read(td)
    assert_array_equal(vdata, rdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)

    # agilent -> pipe
    cdic, cdata = vC.to_pipe()
    assert_array_equal(pdata, cdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata)
    bpk = list(bad_pipe_keys)
    bpk.append("FDDISPMAX")     # nmrglue doesn't update the MIN/MAX values
    bpk.append("FDMIN")
    bpk.append("FDDISPMIN")
    bpk.append("FDSCALEFLAG")
    bpk.append("FDMAX")
    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    check_pdic(pdic, cdic, bpk)
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> agilent
    cdic, cdata = pC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rdic, rdata = ng.varian.read(td)
    assert_array_equal(vdata, rdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_agilent_3d_rnmrtk():
    """ 3D time agilent, rnmrtk <-> rnmrtk """
    # prepare agilent converter
    vdic, vdata = ng.varian.read(os.path.join(DATA_DIR, "agilent_3d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare rnmrtk converter
    rdic, rdata = ng.rnmrtk.read(os.path.join(DATA_DIR, 'rnmrtk_3d',
                                              'time_3d.sec'))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic, agilent_compatible=True)

    # agilent -> rnmrtk
    cdic, cdata = vC.to_rnmrtk(agilent_compatible=True)
    assert_array_equal(rdata, cdata)
    # check_rdic(rdic, cdic, 3, bad_rnmrtk_keys)     # XXX do not check
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(cdata, rrdata)
    check_rdic(cdic, rrdic, 3)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk(agilent_compatible=True)
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 3, bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    check_rdic(rdic, rrdic, 3, bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> agilent
    cdic, cdata = rC.to_varian()
    assert_array_equal(vdata, cdata)
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write(td, cdic, cdata)
    rrdic, rrdata = ng.varian.read(td)
    assert_array_equal(vdata, rrdata)
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_bruker_1d():
    """ 1D time bruker, pipe <-> bruker, pipe """
    # prepare Bruker converter
    bdic, bdata = ng.bruker.read(os.path.join(DATA_DIR, "bruker_1d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "bruker_1d",
                               "test.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # bruker -> bruker
    cdic, cdata = bC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    shutil.rmtree(td)

    # bruker -> pipe
    cdic, cdata = bC.to_pipe()
    assert_array_equal(pdata, cdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata)
    # bpdk = list(bad_pipe_keys)
    # bpdk.append("FDF2ORIG")         # these are roundoff errors
    # bpdk.append("FDFLTORDER")       # not a problem when written
    check_pdic(pdic, cdic, bad_pipe_keys)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    check_pdic(pdic, cdic, bad_pipe_keys)
    os.remove(tf)

    # pipe -> bruker
    cdic, cdata = pC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)


def test_bruker_1d_rnmrtk():
    """ 1D time bruker, rnmrtk <-> rnmrtk """
    # prepare Bruker converter
    bdic, bdata = ng.bruker.read(os.path.join(DATA_DIR, "bruker_1d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    rdic, rdata = ng.rnmrtk.read(os.path.join(DATA_DIR, "bruker_1d",
                                 "time_1d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic)

    # bruker -> rnmrtk
    cdic, cdata = bC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    # check_rdic(rdic, cdic, 1)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    # check_pdic(rdic, rrdic , 1)   # XXX don't check dictionary
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 1, bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    check_rdic(rdic, rrdic, 1, bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> bruker
    cdic, cdata = rC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)


def test_bruker_2d():
    """ 2D time bruker, pipe <-> bruker, pipe """
    # prepare Bruker converter
    bdic, bdata = ng.bruker.read(os.path.join(DATA_DIR, "bruker_2d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "bruker_2d",
                                            "test.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # bruker -> bruker
    cdic, cdata = bC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    shutil.rmtree(td)

    # bruker -> pipe
    cdic, cdata = bC.to_pipe()
    assert_array_equal(pdata, cdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata)
    bpk = list(bad_pipe_keys)
    bpk.append("FDREALSIZE")    # NMRPipe corrects sizes for oversampling
    bpk.append("FDF2APOD")
    bpk.append("FDF2TDSIZE")
    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    check_pdic(pdic, cdic, bpk, v=True)
    os.remove(tf)

    # pipe -> bruker
    cdic, cdata = pC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)


def test_bruker_2d_rnmrtk():
    """ 2D time bruker, rnmrtk <-> rnmrtk """
    # prepare Bruker converter
    bdic, bdata = ng.bruker.read(os.path.join(DATA_DIR, "bruker_2d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    rdic, rdata = ng.rnmrtk.read(os.path.join(DATA_DIR, "bruker_2d",
                                              "time_2d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic)

    # bruker -> rnmrtk
    cdic, cdata = bC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    # check_rdic(rdic, cdic, 1)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    # check_pdic(rdic, rrdic , 1)   # XXX don't check dictionary
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 2, bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    check_rdic(rdic, rrdic, 2, bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> bruker
    cdic, cdata = rC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)


def test_bruker_3d():
    """ 3D time bruker, pipe <-> bruker, pipe """

    # copy the acqu2s file to acqu3s and modify it for testing.
    # this is a hack until more complete datasets can be added for testing
    acqu3s = os.path.join(DATA_DIR, "bruker_3d", "acqu3s")
    shutil.copy2(os.path.join(DATA_DIR, "bruker_3d", "acqu2s"), acqu3s)
    with open(acqu3s) as f:
        out_name = acqu3s + ".tmp"
        out = open(out_name, 'w')
        for line in f:
            line = sub("##ORIGIN= .+",
                       "##ORIGIN= Fake acqu3s file generated for testing",
                       line)
            line = sub(r"\$BF1.+",
                       "$BF1= 201.192849",
                       line)
            line = sub(r"\$NUC1.+",
                       "$NUC1= <13C>",
                       line)
            line = sub(r"\$O1.+",
                       "$O1= 10663.220997003",
                       line)
            line = sub(r"\$SFO1.+",
                       "$SFO1= 201.203512220997",
                       line)
            line = sub(r"\$SW=.+",
                       "$SW=27.611626113",
                       line)
            line = sub(r"\$SW_h.+",
                       "$SW_h= 5555.556152",
                       line)
            out.write(line)
        out.close()
        os.rename(out_name, acqu3s)

    # prepare Bruker converter
    bdic, bdata = ng.bruker.read(os.path.join(DATA_DIR, "bruker_3d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "bruker_3d", "fid",
                                            "test%03d.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # bruker -> bruker
    cdic, cdata = bC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    shutil.rmtree(td)

    # bruker -> pipe
    cdic, cdata = bC.to_pipe()
    assert_array_equal(pdata, cdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata)
    bpk = list(bad_pipe_keys)
    bpk.append("FDDISPMAX")     # nmrglue doesn't update the MIN/MAX values
    bpk.append("FDMIN")
    bpk.append("FDDISPMIN")
    bpk.append("FDSCALEFLAG")
    bpk.append("FDMAX")
    bpk.append("FDREALSIZE")    # NMRPipe corrects sizes for oversampling
    bpk.append("FDF2APOD")
    bpk.append("FDF2TDSIZE")
    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    check_pdic(pdic, cdic, bpk, v=True)
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> bruker
    cdic, cdata = pC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)

    os.remove(acqu3s)


def test_bruker_3d_rnmrtk():
    """ 3D time bruker, rnmrtk <-> rnmrtk """
    # prepare Bruker converter
    bdic, bdata = ng.bruker.read(os.path.join(DATA_DIR, "bruker_3d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    rdic, rdata = ng.rnmrtk.read(os.path.join(DATA_DIR, "bruker_3d",
                                              "time_3d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic)

    # bruker -> rnmrtk
    cdic, cdata = bC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    # check_rdic(rdic, cdic, 3)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    # check_pdic(rdic, rrdic , 3)   # XXX don't check dictionary
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 3, bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rdata, rrdata)
    check_rdic(rdic, rrdic, 3, bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> bruker
    cdic, cdata = rC.to_bruker()
    assert_array_equal(bdata, cdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write(td, cdic, cdata)
    rdic, rdata = ng.bruker.read(td)
    assert_array_equal(bdata, rdata)
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)


def test_sparky_2d():
    """ 2D freq sparky, pipe <-> sparky, pipe """
    # prepare Sparky converter
    sdic, sdata = ng.sparky.read(os.path.join(DATA_DIR,  "sparky_2d",
                                              "data.ucsf"))
    ubdic = ng.sparky.guess_udic(sdic, sdata)
    sC = ng.convert.converter()
    sC.from_sparky(sdic, sdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR,  "nmrpipe_2d",
                                            "test.ft2"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # sparky -> sparky
    cdic, cdata = sC.to_sparky()
    assert_array_equal(sdata, cdata)
    check_sdic(sdic, cdic, bad_sparky_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read(tf)
    assert_array_equal(sdata, rdata)
    check_sdic(sdic, rdic, bad_sparky_keys, v=True)
    os.remove(tf)

    # sparky -> pipe
    cdic, cdata = sC.to_pipe()
    assert_array_equal(pdata, cdata[:])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata[:])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata[:])
    bpk = list(bad_pipe_keys)
    bpk.append("FDF1TDSIZE")    # we lose all processing information
    bpk.append("FDF1APOD")
    bpk.append("FDF1ZF")
    bpk.append("FDF1C1")
    bpk.append("FDF1APODCODE")
    bpk.append("FDF1APODQ1")
    bpk.append("FDF1APODQ2")
    bpk.append("FDF1APODQ3")
    bpk.append("FDF2P0")
    bpk.append("FDF2APOD")
    bpk.append("FDF2ZF")
    bpk.append("FDF2APODCODE")
    bpk.append("FDF2APODQ1")
    bpk.append("FDF2APODQ2")
    bpk.append("FDF2APODQ3")
    bpk.append("FDSLICECOUNT")
    bpk.append("FDREALSIZE")
    bpk.append("FDF2TDSIZE")

    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata[:])
    check_pdic(pdic, cdic, bpk)
    os.remove(tf)

    # pipe -> sparky
    cdic, cdata = pC.to_sparky()
    assert_array_equal(sdata, cdata[:])
    check_sdic(sdic, cdic, bad_sparky_keys, True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read(tf)
    assert_array_equal(sdata, rdata[:])
    check_sdic(sdic, rdic, bad_sparky_keys, True)
    os.remove(tf)


def test_sparky_3d():
    """ 3D freq sparky, pipe <-> sparky, pipe """
    # prepare Sparky converter
    sdic, sdata = ng.sparky.read(os.path.join(DATA_DIR, "sparky_3d",
                                              "data.ucsf"))
    ubdic = ng.sparky.guess_udic(sdic, sdata)
    sC = ng.convert.converter()
    sC.from_sparky(sdic, sdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "nmrpipe_3d", "ft",
                                            "test%03d.ft3"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # sparky -> sparky
    cdic, cdata = sC.to_sparky()
    assert_array_equal(sdata, cdata)
    check_sdic(sdic, cdic, bad_sparky_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read(tf)
    assert_array_equal(sdata, rdata)
    check_sdic(sdic, rdic, bad_sparky_keys, v=True)
    os.remove(tf)

    # sparky -> pipe
    cdic, cdata = sC.to_pipe()
    assert_array_equal(pdata, cdata[:])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata[:])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    for f in glob.glob(tf[:-4]+"*"):
        os.remove(f)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata[:])
    bpk = list(bad_pipe_keys)
    bpk.append("FDDISPMAX")     # nmrglue doesn't update the MIN/MAX values
    bpk.append("FDMIN")
    bpk.append("FDDISPMIN")
    bpk.append("FDSCALEFLAG")
    bpk.append("FDMAX")

    bpk.append("FDF1TDSIZE")    # we lose all processing information
    bpk.append("FDF1APOD")
    bpk.append("FDF1ZF")

    bpk.append("FDF2TDSIZE")
    bpk.append("FDF2APOD")
    bpk.append("FDF2ZF")

    bpk.append("FDF3TDSIZE")
    bpk.append("FDF3APOD")
    bpk.append("FDF3ZF")
    bpk.append("FDF3P0")
    bpk.append("FDF3P1")

    bpk.append("FDREALSIZE")

    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata[:])
    check_pdic(pdic, cdic, bpk)
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> sparky
    cdic, cdata = pC.to_sparky()
    assert_array_equal(sdata, cdata[:])
    bsk = list(bad_sparky_keys)
    # the NMRPipe nucleus labels are passed to sparky not 13C, 15N, etc
    bsk.append("nucleus")
    check_sdic(sdic, cdic, bsk, True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read(tf)
    assert_array_equal(sdata, rdata[:])
    check_sdic(sdic, rdic, bsk, True)
    os.remove(tf)


def test_pipe_1d():
    """ 1D freq pipe <-> pipe """
    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(os.path.join(DATA_DIR, "nmrpipe_1d",
                                            "test.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata)
    check_pdic(pdic, cdic, bad_pipe_keys)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rdata)
    check_pdic(pdic, cdic, bad_pipe_keys)
    os.remove(tf)


def test_csdm_1d():
    """Test 1D bruker and agilent -> CSDM"""
    # 1D bruker
    bdic1, bdata1 = ng.bruker.read(os.path.join(DATA_DIR, "bruker_1d"))
    ubdic1 = ng.bruker.guess_udic(bdic1, bdata1)
    bC1 = ng.convert.converter()
    bC1.from_bruker(bdic1, bdata1, ubdic1)
    csdm_data = bC1.to_csdm()
    assert len(csdm_data.dimensions) == 1
    assert len(csdm_data.dependent_variables) == 1
    assert csdm_data.dimensions[0].count == ubdic1[0]["size"]
    assert csdm_data.dimensions[0].increment.value == 1 / ubdic1[0]["sw"]
    assert (
        csdm_data.dimensions[0].reciprocal.coordinates_offset.value == ubdic1[0]["car"]
    )
    assert csdm_data.dimensions[0].reciprocal.origin_offset.value == ubdic1[0]["obs"]
    assert csdm_data.dimensions[0].label == ubdic1[0]["label"]
    assert_array_equal(csdm_data.dependent_variables[0].components[0], bdata1)

    # 1D agilent
    adic1, adata1 = ng.agilent.read(os.path.join(DATA_DIR, "agilent_1d"))
    uadic1 = ng.agilent.guess_udic(adic1, adata1)
    aC1 = ng.convert.converter()
    aC1.from_varian(adic1, adata1, uadic1)
    csdm_data = aC1.to_csdm()
    assert len(csdm_data.dimensions) == 1
    assert len(csdm_data.dependent_variables) == 1
    assert csdm_data.dimensions[0].count == uadic1[0]["size"]
    assert csdm_data.dimensions[0].increment.value == 1 / uadic1[0]["sw"]
    assert (
        csdm_data.dimensions[0].reciprocal.coordinates_offset.value == uadic1[0]["car"]
    )
    assert csdm_data.dimensions[0].reciprocal.origin_offset.value == uadic1[0]["obs"]
    assert csdm_data.dimensions[0].label == uadic1[0]["label"]
    assert_array_equal(csdm_data.dependent_variables[0].components[0], adata1)


def test_csdm_2d():
    """Test 2D bruker and agilent -> CSDM"""
    # 2D bruker
    bdic2, bdata2 = ng.bruker.read(os.path.join(DATA_DIR, "bruker_2d"))
    ubdic2 = ng.bruker.guess_udic(bdic2, bdata2)
    bC2 = ng.convert.converter()
    bC2.from_bruker(bdic2, bdata2, ubdic2)
    csdm_data = bC2.to_csdm()
    assert len(csdm_data.dimensions) == 2
    assert len(csdm_data.dependent_variables) == 1
    for i in range(2):
        j = 1 - i
        assert csdm_data.dimensions[j].count == ubdic2[i]["size"]
        assert csdm_data.dimensions[j].increment.value == 1 / ubdic2[i]["sw"]
        assert (
            csdm_data.dimensions[j].reciprocal.coordinates_offset.value
            == ubdic2[i]["car"]
        )
        assert (
            csdm_data.dimensions[j].reciprocal.origin_offset.value == ubdic2[i]["obs"]
        )
        assert csdm_data.dimensions[j].label == ubdic2[i]["label"]
    assert_array_equal(csdm_data.dependent_variables[0].components[0], bdata2)

    # 2D agilent
    adic2, adata2 = ng.varian.read(os.path.join(DATA_DIR, "agilent_2d"))
    uadic2 = ng.varian.guess_udic(adic2, adata2)
    aC2 = ng.convert.converter()
    aC2.from_varian(adic2, adata2, uadic2)
    csdm_data = aC2.to_csdm()
    assert len(csdm_data.dimensions) == 2
    assert len(csdm_data.dependent_variables) == 1
    for i in range(2):
        j = 1 - i
        assert csdm_data.dimensions[j].count == uadic2[i]["size"]
        assert csdm_data.dimensions[j].increment.value == 1 / uadic2[i]["sw"]
        assert (
            csdm_data.dimensions[j].reciprocal.coordinates_offset.value
            == uadic2[i]["car"]
        )
        assert (
            csdm_data.dimensions[j].reciprocal.origin_offset.value == uadic2[i]["obs"]
        )
        assert csdm_data.dimensions[j].label == uadic2[i]["label"]
    assert_array_equal(csdm_data.dependent_variables[0].components[0], adata2)


def test_csdm_3d():
    """Test 3D bruker and agilent -> CSDM"""
    # 3D bruker
    bdic3, bdata3 = ng.bruker.read(os.path.join(DATA_DIR, "bruker_3d"))
    ubdic3 = ng.bruker.guess_udic(bdic3, bdata3)
    bC3 = ng.convert.converter()
    bC3.from_bruker(bdic3, bdata3, ubdic3)
    csdm_data = bC3.to_csdm()
    assert len(csdm_data.dimensions) == 3
    assert len(csdm_data.dependent_variables) == 1
    for j in range(3):
        i = 2 - j
        assert csdm_data.dimensions[j].count == ubdic3[i]["size"]
        assert csdm_data.dimensions[j].increment.value == 1 / ubdic3[i]["sw"]
        assert (
            csdm_data.dimensions[j].reciprocal.coordinates_offset.value
            == ubdic3[i]["car"]
        )
        assert (
            csdm_data.dimensions[j].reciprocal.origin_offset.value == ubdic3[i]["obs"]
        )
        assert csdm_data.dimensions[j].label == ubdic3[i]["label"]
    assert_array_equal(csdm_data.dependent_variables[0].components[0], bdata3)

    # 3D agilent
    adic3, adata3 = ng.varian.read(os.path.join(DATA_DIR, "agilent_3d"))
    uadic3 = ng.varian.guess_udic(adic3, adata3)
    aC3 = ng.convert.converter()
    aC3.from_varian(adic3, adata3)
    csdm_data = aC3.to_csdm()
    assert len(csdm_data.dimensions) == 3
    assert len(csdm_data.dependent_variables) == 1
    for j in range(3):
        i = 2 - j
        print(uadic3)
        print(adata3)
        # print(csdm_data.dimensions[0].increment.value)
        # print(1 / uadic3[0]["sw"])
        # print(csdm_datacl.dimensions[1].increment.value)
        # print(1 / uadic3[1]["sw"])
        # print(csdm_data.dimensions[2].increment.value)
        # print(1 / uadic3[2]["sw"])
        print(csdm_data)
        assert csdm_data.dimensions[j].count == uadic3[i]["size"]
        assert csdm_data.dimensions[j].increment.value == 1 / uadic3[i]["sw"]
        assert (
            csdm_data.dimensions[j].reciprocal.coordinates_offset.value
            == uadic3[i]["car"]
        )
        assert (
            csdm_data.dimensions[j].reciprocal.origin_offset.value == uadic3[i]["obs"]
        )
        assert csdm_data.dimensions[j].label == uadic3[i]["label"]
    assert_array_equal(csdm_data.dependent_variables[0].components[0], adata3)


# lowmemory tests ###
def test_sparky_2d_lowmem():
    """ 2D freq sparky, pipe <-> sparky, pipe low memory"""
    # prepare Sparky converter
    sdic, sdata = ng.sparky.read_lowmem(
        os.path.join(DATA_DIR, "sparky_2d", "data.ucsf"))
    ubdic = ng.sparky.guess_udic(sdic, sdata)
    sC = ng.convert.converter()
    sC.from_sparky(sdic, sdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read_lowmem(
        os.path.join(DATA_DIR, "nmrpipe_2d", "test.ft2"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # sparky -> sparky
    cdic, cdata = sC.to_sparky()
    assert_array_equal(sdata[0:3, 0:4], cdata[0:3, 0:4])
    check_sdic(sdic, cdic, bad_sparky_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read_lowmem(tf)
    assert_array_equal(sdata[0:3, 0:4], rdata[0:3, 0:4])
    check_sdic(sdic, rdic, bad_sparky_keys, v=True)
    os.remove(tf)

    # sparky -> pipe
    cdic, cdata = sC.to_pipe()
    assert_array_equal(pdata[0:3, 0:4], cdata[0:3, 0:4])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    # XXX trace by trace writing from sparky is very slow
    ng.pipe.write(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:3, 0:4], rdata[0:3, 0:4])
    # check_pdic(pdic,cdic,v=True)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata[0:3, 0:4], cdata[0:3, 0:4])
    bpk = list(bad_pipe_keys)
    bpk.append("FDF1TDSIZE")    # we lose all processing information
    bpk.append("FDF1APOD")
    bpk.append("FDF1ZF")
    bpk.append("FDF1C1")
    bpk.append("FDF1APODCODE")
    bpk.append("FDF1APODQ1")
    bpk.append("FDF1APODQ2")
    bpk.append("FDF1APODQ3")
    bpk.append("FDF2P0")
    bpk.append("FDF2APOD")
    bpk.append("FDF2ZF")
    bpk.append("FDF2APODCODE")
    bpk.append("FDF2APODQ1")
    bpk.append("FDF2APODQ2")
    bpk.append("FDF2APODQ3")
    bpk.append("FDSLICECOUNT")
    bpk.append("FDREALSIZE")
    bpk.append("FDF2TDSIZE")

    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:3, 0:4], rdata[0:3, 0:4])
    check_pdic(pdic, cdic, bpk)
    os.remove(tf)

    # pipe -> sparky
    cdic, cdata = pC.to_sparky()
    assert_array_equal(sdata[0:3, 0:4], cdata[0:3, 0:4])
    check_sdic(sdic, cdic, bad_sparky_keys, True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read_lowmem(tf)
    assert_array_equal(sdata[0:3, 0:4], rdata[0:3, 0:4])
    check_sdic(sdic, rdic, bad_sparky_keys, True)
    os.remove(tf)


def test_sparky_3d_lowmem():
    """ 3D freq sparky, pipe <-> sparky, pipe low memory"""
    # prepare Sparky converter
    sdic, sdata = ng.sparky.read_lowmem(
        os.path.join(DATA_DIR,  "sparky_3d", "data.ucsf"))
    ubdic = ng.sparky.guess_udic(sdic, sdata)
    sC = ng.convert.converter()
    sC.from_sparky(sdic, sdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read_lowmem(
        os.path.join(DATA_DIR, "nmrpipe_3d", "ft", "test%03d.ft3"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # sparky -> sparky
    cdic, cdata = sC.to_sparky()
    assert_array_equal(sdata[0:3, 0:4, 0:5], cdata[0:3, 0:4, 0:5])
    check_sdic(sdic, cdic, bad_sparky_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read_lowmem(tf)
    assert_array_equal(sdata[0:3, 0:4, 0:5], rdata[0:3, 0:4, 0:5])
    check_sdic(sdic, rdic, bad_sparky_keys, v=True)
    os.remove(tf)

    # sparky -> pipe
    cdic, cdata = sC.to_pipe()
    assert_array_equal(pdata[0:3, 0:4, 0:5], cdata[0:3, 0:4, 0:5])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    # XXX trace by trace writing from sparky is very slow.
    # tf = tempfile.mktemp(dir=".") + "%03d"
    # ng.pipe.write_lowmem(tf, cdic, cdata)
    # rdic, rdata = ng.pipe.read_lowmem(tf)
    # assert_array_equal(pdata, rdata[:])
    # check_pdic(pdic, cdic)   # XXX don't check dictionary
    # for f in glob.glob(tf[:-4] + "*"):
    #     os.remove(f)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata[0:3, 0:4, 0:5], cdata[0:3, 0:4, 0:5])
    bpk = list(bad_pipe_keys)
    bpk.append("FDDISPMAX")     # nmrglue doesn't update the MIN/MAX values
    bpk.append("FDMIN")
    bpk.append("FDDISPMIN")
    bpk.append("FDSCALEFLAG")
    bpk.append("FDMAX")

    bpk.append("FDF1TDSIZE")    # we lose all processing information
    bpk.append("FDF1APOD")
    bpk.append("FDF1ZF")

    bpk.append("FDF2TDSIZE")
    bpk.append("FDF2APOD")
    bpk.append("FDF2ZF")

    bpk.append("FDF3TDSIZE")
    bpk.append("FDF3APOD")
    bpk.append("FDF3ZF")
    bpk.append("FDF3P0")
    bpk.append("FDF3P1")

    bpk.append("FDREALSIZE")

    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:3, 0:4, 0:5], rdata[0:3, 0:4, 0:5])
    check_pdic(pdic, cdic, bpk)
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> sparky
    cdic, cdata = pC.to_sparky()
    assert_array_equal(sdata[0:3, 0:4, 0:5], cdata[0:3, 0:4, 0:5])
    bsk = list(bad_sparky_keys)
    bsk.append("nucleus")
    # the NMRPipe nucleus labels are passed to sparky not 13C, 15N, etc
    check_sdic(sdic, cdic, bsk, True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.sparky.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.sparky.read_lowmem(tf)
    assert_array_equal(sdata[0:3, 0:4, 0:5], rdata[0:3, 0:4, 0:5])
    check_sdic(sdic, rdic, bsk, True)
    os.remove(tf)


def test_bruker_2d_lowmem():
    """ 2D time bruker, pipe <-> bruker, pipe low memory"""
    # prepare Bruker converter
    bdic, bdata = ng.bruker.read_lowmem(
        os.path.join(DATA_DIR, "bruker_2d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read_lowmem(
        os.path.join(DATA_DIR, "bruker_2d", "test.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # bruker -> bruker
    cdic, cdata = bC.to_bruker()
    assert_array_equal(bdata[0:3, 100:200], cdata[0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.bruker.read_lowmem(td)
    assert_array_equal(bdata[0:3, 100:200], rdata[0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    shutil.rmtree(td)

    # bruker -> pipe
    cdic, cdata = bC.to_pipe()
    assert_array_equal(pdata[0:3, 100:200], cdata[0:3, 100:200])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:3, 100:200], rdata[0:3, 100:200])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata[0:3, 100:200], cdata[0:3, 100:200])
    bpk = list(bad_pipe_keys)
    bpk.append("FDREALSIZE")    # NMRPipe corrects sizes for oversampling
    bpk.append("FDF2APOD")
    bpk.append("FDF2TDSIZE")
    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:3, 100:200], rdata[0:3, 100:200])
    check_pdic(pdic, cdic, bpk, v=True)
    os.remove(tf)

    # pipe -> bruker
    cdic, cdata = pC.to_bruker()
    assert_array_equal(bdata[0:3, 100:200], cdata[0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.bruker.read_lowmem(td)
    assert_array_equal(bdata[0:3, 100:200], rdata[0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)


def test_bruker_3d_lowmem():
    """ 3D time bruker, pipe <-> bruker, pipe low memory"""

    # copy the acqu2s file to acqu3s and modify it for testing.
    # this is a hack until more complete datasets can be added for testing
    acqu3s = os.path.join(DATA_DIR, "bruker_3d", "acqu3s")
    shutil.copy2(os.path.join(DATA_DIR, "bruker_3d", "acqu2s"), acqu3s)
    with open(acqu3s) as f:
        out_name = acqu3s + ".tmp"
        out = open(out_name, 'w')
        for line in f:
            line = sub("##ORIGIN= .+",
                       "##ORIGIN= Fake acqu3s file generated for testing",
                       line)
            line = sub(r"\$BF1.+",
                       "$BF1= 201.192849",
                       line)
            line = sub(r"\$NUC1.+",
                       "$NUC1= <13C>",
                       line)
            line = sub(r"\$O1.+",
                       "$O1= 10663.220997003",
                       line)
            line = sub(r"\$SFO1.+",
                       "$SFO1= 201.203512220997",
                       line)
            line = sub(r"\$SW=.+",
                       "$SW=27.611626113",
                       line)
            line = sub(r"\$SW_h.+",
                       "$SW_h= 5555.556152",
                       line)
            out.write(line)
        out.close()
        os.rename(out_name, acqu3s)

    # prepare Bruker converter
    bdic, bdata = ng.bruker.read_lowmem(
        os.path.join(DATA_DIR, "bruker_3d"))
    ubdic = ng.bruker.guess_udic(bdic, bdata)
    bC = ng.convert.converter()
    bC.from_bruker(bdic, bdata, ubdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read_lowmem(
        os.path.join(DATA_DIR, "bruker_3d", "fid", "test%03d.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # bruker -> bruker
    cdic, cdata = bC.to_bruker()
    assert_array_equal(bdata[0:2, 0:3, 100:200], cdata[0:2, 0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.bruker.read_lowmem(td)
    assert_array_equal(bdata[0:2, 0:3, 100:200], rdata[0:2, 0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys, v=True)
    shutil.rmtree(td)

    # bruker -> pipe
    cdic, cdata = bC.to_pipe()
    assert_array_equal(pdata[0:2, 0:3, 100:200], cdata[0:2, 0:3, 100:200])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:2, 0:3, 100:200], rdata[0:2, 0:3, 100:200])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata[0:2, 0:3, 100:200], cdata[0:2, 0:3, 100:200])
    bpk = list(bad_pipe_keys)
    bpk.append("FDDISPMAX")     # nmrglue doesn't update the MIN/MAX values
    bpk.append("FDMIN")
    bpk.append("FDDISPMIN")
    bpk.append("FDSCALEFLAG")
    bpk.append("FDMAX")
    bpk.append("FDREALSIZE")    # NMRPipe corrects sizes for oversampling
    bpk.append("FDF2APOD")
    bpk.append("FDF2TDSIZE")
    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:2, 0:3, 100:200], rdata[0:2, 0:3, 100:200])
    check_pdic(pdic, cdic, bpk, v=True)
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> bruker
    cdic, cdata = pC.to_bruker()
    assert_array_equal(bdata[0:2, 0:3, 100:200], cdata[0:2, 0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.bruker.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.bruker.read_lowmem(td)
    assert_array_equal(bdata[0:2, 0:3, 100:200], rdata[0:2, 0:3, 100:200])
    check_dic(bdic, cdic, bad_bruker_keys)
    shutil.rmtree(td)

    os.remove(acqu3s)


def test_agilent_2d_lowmem():
    """ 2D time agilent, pipe <-> agilent, pipe low memory"""
    # prepare Varian converter
    vdic, vdata = ng.varian.read_lowmem(
        os.path.join(DATA_DIR, "agilent_2d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read_lowmem(
        os.path.join(DATA_DIR, "agilent_2d", "test.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # varian -> varian
    cdic, cdata = vC.to_varian()
    assert_array_equal(vdata[0:4, 0:20], cdata[0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.varian.read_lowmem(td)
    assert_array_equal(vdata[0:4, 0:20], rdata[0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)

    # varian -> pipe
    cdic, cdata = vC.to_pipe()
    assert_array_equal(pdata[0:4, 0:20], cdata[0:4, 0:20])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:4, 0:20], rdata[0:4, 0:20])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata[0:4, 0:20], cdata[0:4, 0:20])
    check_pdic(pdic, cdic, bad_pipe_keys)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:4, 0:20], rdata[0:4, 0:20])
    check_pdic(pdic, cdic, bad_pipe_keys)
    os.remove(tf)

    # pipe -> varian
    cdic, cdata = pC.to_varian()
    assert_array_equal(vdata[0:4, 0:20], cdata[0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.varian.read_lowmem(td)
    assert_array_equal(vdata[0:4, 0:20], rdata[0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_agilent_3d_lowmem():
    """ 3D time agilent, pipe <-> agilent, pipe low memory"""
    # prepare Agilent converter
    vdic, vdata = ng.varian.read_lowmem(
        os.path.join(DATA_DIR, "agilent_3d"))
    uvdic = ng.varian.guess_udic(vdic, vdata)
    vC = ng.convert.converter()
    vC.from_varian(vdic, vdata, uvdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read_lowmem(
        os.path.join(DATA_DIR, "agilent_3d", "data", "test%03d.fid"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # agilent -> agilent
    cdic, cdata = vC.to_varian()
    assert_array_equal(vdata[0:3, 0:4, 0:20], cdata[0:3, 0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.varian.read_lowmem(td)
    assert_array_equal(vdata[0:3, 0:4, 0:20], rdata[0:3, 0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)

    # agilent -> pipe
    cdic, cdata = vC.to_pipe()
    assert_array_equal(pdata[0:3, 0:4, 0:20], cdata[0:3, 0:4, 0:20])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:3, 0:4, 0:20], rdata[0:3, 0:4, 0:20])
    # check_pdic(pdic,cdic)   # XXX don't check dictionary
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata[0:3, 0:4, 0:20], cdata[0:3, 0:4, 0:20])
    bpk = list(bad_pipe_keys)
    bpk.append("FDDISPMAX")     # nmrglue doesn't update the MIN/MAX values
    bpk.append("FDMIN")
    bpk.append("FDDISPMIN")
    bpk.append("FDSCALEFLAG")
    bpk.append("FDMAX")
    check_pdic(pdic, cdic, bpk, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    ng.pipe.write_lowmem(tf, cdic, cdata)
    rdic, rdata = ng.pipe.read_lowmem(tf)
    assert_array_equal(pdata[0:3, 0:4, 0:20], rdata[0:3, 0:4, 0:20])
    check_pdic(pdic, cdic, bpk)
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> varian
    cdic, cdata = pC.to_varian()
    assert_array_equal(vdata[0:3, 0:4, 0:20], cdata[0:3, 0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    # write and readback
    td = tempfile.mkdtemp(dir=".")
    ng.varian.write_lowmem(td, cdic, cdata)
    rdic, rdata = ng.varian.read_lowmem(td)
    assert_array_equal(vdata[0:3, 0:4, 0:20], rdata[0:3, 0:4, 0:20])
    check_dic(vdic, cdic, bad_varian_keys)
    shutil.rmtree(td)


def test_rnmrtk_1d():
    """ 1D freq rnmrtk, pipe <-> rnmrtk, pipe """

    # prepare rnmrtk converter
    rdic, rdata = ng.rnmrtk.read(
        os.path.join(DATA_DIR, "rnmrtk_1d", "freq_1d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic)

    # prepare Pipe converter
    pdic, pdata = ng.pipe.read(
        os.path.join(DATA_DIR, "rnmrtk_1d", "test.ft"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 1, exclude=bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(cdata, rrdata)
    check_rdic(rdic, rrdic, 1, exclude=bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> pipe
    cdic, cdata = rC.to_pipe()
    assert_array_equal(pdata, cdata)
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rrdic, rrdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rrdata)
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata[:])
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rrdic, rrdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rrdata[:])
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    os.remove(tf)

    # pipe -> rnmrtk
    cdic, cdata = pC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 1, exclude=bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rrdata, rdata)
    check_rdic(rdic, rrdic, 1, exclude=bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))


def test_rnmrtk_2d():
    """ 2D freq rnmrtk, pipe <-> rnmrtk, pipe """

    # prepare rnmrtk converter
    rdic, rdata = ng.rnmrtk.read(
        os.path.join(DATA_DIR, "rnmrtk_2d", "freq_2d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic)

    # prepare pipe converter
    pdic, pdata = ng.pipe.read(
        os.path.join(DATA_DIR, "rnmrtk_2d", "test.ft2"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 2, exclude=bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(cdata, rrdata)
    check_rdic(rdic, rrdic, 2, exclude=bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> pipe
    cdic, cdata = rC.to_pipe()
    assert_array_equal(pdata, cdata)
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rrdic, rrdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rrdata)
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    os.remove(tf)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata[:])
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".")
    ng.pipe.write(tf, cdic, cdata)
    rrdic, rrdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rrdata[:])
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    os.remove(tf)

    # pipe -> rnmrtk
    cdic, cdata = pC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 2, exclude=bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rrdata, rdata)
    check_rdic(rdic, rrdic, 2, exclude=bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))


def test_rnmrtk_3d():
    """ 3D freq rnmrtk, pipe <-> rnmrtk, pipe """

    # prepare rnmrtk converter
    rdic, rdata = ng.rnmrtk.read(
        os.path.join(DATA_DIR, "rnmrtk_3d", "freq_3d.sec"))
    urdic = ng.rnmrtk.guess_udic(rdic, rdata)
    rC = ng.convert.converter()
    rC.from_rnmrtk(rdic, rdata, urdic)

    # prepare pipe converter
    pdic, pdata = ng.pipe.read(
        os.path.join(DATA_DIR, "rnmrtk_3d", "test.ft3"))
    updic = ng.pipe.guess_udic(pdic, pdata)
    pC = ng.convert.converter()
    pC.from_pipe(pdic, pdata, updic)

    # rnmrtk -> rnmrtk
    cdic, cdata = rC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 3, exclude=bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(cdata, rrdata)
    check_rdic(rdic, rrdic, 3, exclude=bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))

    # rnmrtk -> pipe
    cdic, cdata = rC.to_pipe()
    assert_array_equal(pdata, cdata)
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    # tf = tempfile.mktemp(dir=".")      # Uncomment these lines to write
    # cdic['FDPIPEFLAG'] = 1.0           # a single NMRPipe stream file
    ng.pipe.write(tf, cdic, cdata)
    rrdic, rrdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rrdata)
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # os.remove(tf)                      # this line too
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> pipe
    cdic, cdata = pC.to_pipe()
    assert_array_equal(pdata, cdata[:])
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # write and readback
    tf = tempfile.mktemp(dir=".") + "%03d"
    # tf = tempfile.mktemp(dir=".")  # Uncomment these lines to write
    # cdic['FDPIPEFLAG'] = 1.0       # a single NMRPipe stream file
    ng.pipe.write(tf, cdic, cdata)
    rrdic, rrdata = ng.pipe.read(tf)
    assert_array_equal(pdata, rrdata[:])
    check_pdic(pdic, cdic, bad_pipe_keys + bad_rnmrtk2pipe_keys, v=True)
    # os.remove(tf)                  # This line too
    for f in glob.glob(tf[:-4] + "*"):
        os.remove(f)

    # pipe -> rnmrtk
    cdic, cdata = pC.to_rnmrtk()
    assert_array_equal(rdata, cdata)
    check_rdic(rdic, cdic, 3, exclude=bad_rnmrtk_keys)
    # write and readback
    tf = tempfile.mktemp(suffix='.sec', dir='.')
    ng.rnmrtk.write(tf, cdic, cdata)
    rrdic, rrdata = ng.rnmrtk.read(tf)
    assert_array_equal(rrdata, rdata)
    check_rdic(rdic, rrdic, 3, exclude=bad_rnmrtk_keys)
    os.remove(tf)
    os.remove(tf.replace('.sec', '.par'))