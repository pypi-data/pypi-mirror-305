import logging
from pathlib import Path

import hickle
import pytest
from bidict import bidict

from edges_io import io, utils

LOAD_ALIASES = bidict(
    {
        "ambient": "Ambient",
        "hot_load": "HotLoad",
        "open": "LongCableOpen",
        "short": "LongCableShorted",
    }
)

LOGGING = logging.getLogger("edges-io")


@pytest.fixture(scope="module")
def test_dir(tmp_path_factory):
    return test_env(tmp_path_factory)


@pytest.fixture
def test_env(tmp_path_factory):
    # Create an ideal observation file using tmp_path_factory
    path_list = ["Spectra", "Resistance", "S11"]
    s11_list = [
        "Ambient01",
        "AntSim301",
        "HotLoad01",
        "LongCableOpen01",
        "LongCableShorted01",
        "ReceiverReading01",
        "ReceiverReading02",
        "SwitchingState01",
        "SwitchingState02",
    ]
    root_dir = tmp_path_factory.mktemp("Test_Obs")
    obs_dir = root_dir / "Receiver01_25C_2020_01_01_010_to_200MHz"
    obs_dir.mkdir()
    note = obs_dir / "Notes.txt"
    note.touch()
    dlist = []
    slist = []
    for i, p in enumerate(path_list):
        dlist.append(obs_dir / p)
        dlist[i].mkdir()
        if p == "Resistance":
            print("Making Resistance files")
            file_list = [
                "Ambient",
                "AntSim3",
                "HotLoad",
                "LongCableOpen",
                "LongCableShorted",
            ]
            for filename in file_list:
                name1 = filename + "_01_2020_001_01_01_01_lab.csv"
                file1 = dlist[i] / name1
                file1.touch()
        elif p == "S11":
            print("Making S11 files")
            for k, s in enumerate(s11_list):
                slist.append(dlist[i] / s)
                slist[k].mkdir()
                if s[:-2] == "ReceiverReading":
                    file_list = ["ReceiverReading", "Match", "Open", "Short"]
                elif s[:-2] == "SwitchingState":
                    file_list = [
                        "ExternalOpen",
                        "ExternalMatch",
                        "ExternalShort",
                        "Match",
                        "Open",
                        "Short",
                    ]
                else:
                    file_list = ["External", "Match", "Open", "Short"]
                for filename in file_list:
                    name1 = filename + "01.s1p"
                    name2 = filename + "02.s1p"
                    file1 = slist[k] / name1
                    file1.write_text(
                        "# Hz S RI R 50\n"
                        "40000000        0.239144887761343       0.934085904901478\n"
                        "40000000        0.239144887761343       0.934085904901478"
                    )
                    file2 = slist[k] / name2
                    file2.write_text(
                        "# Hz S RI R 50\n"
                        "40000000        0.239144887761343       0.934085904901478\n"
                        "40000000        0.239144887761343       0.934085904901478"
                    )

        elif p == "Spectra":
            print("Making Spectra files")
            file_list = [
                "Ambient",
                "AntSim3",
                "HotLoad",
                "LongCableOpen",
                "LongCableShorted",
            ]
            for filename in file_list:
                name1 = filename + "_01_2020_001_01_01_01_lab.acq"
                file1 = dlist[i] / name1
                file1.touch()
    return obs_dir


# function to make observation object
@pytest.fixture
def calio(test_env):
    return io.CalibrationObservation(test_env)


def test_bad_dirname_obs(test_env, caplog):
    # test that incorrect directories fail

    test_dir = test_env
    base = test_dir.parent

    wrong_dir = base / "Receiver_2020_01_01_010_to_200MHz"
    test_dir.rename(wrong_dir)
    with pytest.raises(utils.FileStructureError):
        io.CalibrationObservation(wrong_dir)
    print(caplog.text)
    assert (
        "The filename Receiver_2020_01_01_010_to_200MHz does not have the correct format"
        in caplog.text
    )

    # receiver number
    test_dir = wrong_dir
    wrong_dir = base / "Receiver00_25C_2020_01_01_010_to_200MHz"
    test_dir.rename(wrong_dir)
    print("WRONGDIR: ", wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "Unknown receiver number" in caplog.text

    # year
    test_dir = wrong_dir
    wrong_dir = base / "Receiver01_25C_2009_01_01_010_to_200MHz"
    test_dir.rename(wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "Unknown year" in caplog.text

    test_dir = wrong_dir
    wrong_dir = base / "Receiver01_25C_2045_01_01_010_to_200MHz"
    test_dir.rename(wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "Unknown year" in caplog.text

    # month
    test_dir = wrong_dir
    wrong_dir = base / "Receiver01_25C_2020_13_01_010_to_200MHz"
    test_dir.rename(wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "Unknown month" in caplog.text

    # day
    test_dir = wrong_dir
    wrong_dir = base / "Receiver01_25C_2020_01_32_010_to_200MHz"
    test_dir.rename(wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "Unknown day" in caplog.text

    # freqlow
    test_dir = wrong_dir
    wrong_dir = base / "Receiver01_25C_2020_01_01_000_to_200MHz"
    test_dir.rename(wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "Low frequency is weird" in caplog.text

    # freqhigh
    test_dir = wrong_dir
    wrong_dir = base / "Receiver01_25C_2020_01_01_010_to_900MHz"
    test_dir.rename(wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "High frequency is weird" in caplog.text

    # freqrange
    test_dir = wrong_dir
    wrong_dir = base / "Receiver01_25C_2020_01_01_200_to_010MHz"
    test_dir.rename(wrong_dir)
    io.CalibrationObservation(wrong_dir)
    assert "Low frequency > High Frequency" in caplog.text


def test_spectra_run_num(datadir: Path):
    spec = io.Spectra(
        datadir / "Receiver01_25C_2019_11_26_040_to_200MHz/Spectra", run_num=1
    )
    assert isinstance(spec.run_num, dict)
    assert all(int(v) == 1 for v in spec.run_num.values())


def test_resistance_run_num(datadir: Path):
    spec = io.Resistances(
        datadir / "Receiver01_25C_2019_11_26_040_to_200MHz/Resistance", run_num=1
    )
    assert isinstance(spec.run_num, dict)
    assert all(int(v) == 1 for v in spec.run_num.values())


def test_list_of_files(datadir: Path):
    obs = datadir / "Receiver01_25C_2019_11_26_040_to_200MHz"
    calobs = io.CalibrationObservation(obs)

    lof = [fl.relative_to(obs.parent) for fl in calobs.list_of_files]

    for fl in lof:
        print(fl)
    assert (
        obs.relative_to(obs.parent)
        / "Resistance"
        / "Ambient_01_2019_329_16_02_35_lab.csv"
        in lof
    )
    assert obs.relative_to(obs.parent) / "S11" / "Ambient01" / "External02.s1p" in lof
    assert (
        obs.relative_to(obs.parent) / "S11" / "Ambient02" / "External02.s1p" not in lof
    )
    assert (
        obs.relative_to(obs.parent) / "S11" / "Ambient01" / "External01.s1p" not in lof
    )


def test_io_partial(datadir: Path):
    obs = datadir / "Receiver01_25C_2023_11_26_040_to_200MHz"

    calobs = io.CalibrationObservation(obs, spectra_kwargs={"filetype": "acq"})
    assert not hasattr(calobs.spectra, "ambient")  # simply nothing there
    assert not hasattr(calobs.spectra, "short")  # wrong format


def test_repeat_num_zero(tmpdir: Path, caplog):
    open_s11 = tmpdir / "Open00.s1p"
    open_s11.touch()

    io.S1P(open_s11)
    print(caplog.records)
    assert "The file Open00.s1p has a repeat_num (00) less than one" in caplog.messages


def test_spectrum_from_load(datadir, caplog):
    spec1 = io.Spectrum.from_load(
        load="ambient",
        direc=datadir / "Receiver01_25C_2019_11_26_040_to_200MHz" / "Spectra",
    )

    spec2 = io.Spectrum.from_load(
        load="Ambient",
        direc=datadir / "Receiver01_25C_2019_11_26_040_to_200MHz" / "Spectra",
    )

    assert spec1 == spec2

    with pytest.raises(utils.LoadExistError):
        io.Spectrum.from_load(
            load="derp",
            direc=datadir / "Receiver01_25C_2019_11_26_040_to_200MHz" / "Spectra",
        )

    assert (
        "The load specified [derp] is not one of the options available."
        in caplog.messages
    )


def test_run_num_not_exist(datadir):
    direc = datadir / "Receiver01_25C_2019_11_26_040_to_200MHz" / "Spectra"
    with pytest.raises(ValueError, match="No Ambient files exist"):
        io.Spectrum.from_load(load="ambient", direc=direc, run_num=2)


def test_spec_matches(datadir):
    spec = io.Spectrum.from_load(
        load="ambient",
        direc=datadir / "Receiver01_25C_2019_11_26_040_to_200MHz" / "Spectra",
    )

    assert spec[0].year == 2019
    assert spec[0].day == 329
    assert spec[0].load_name == "ambient"
    assert spec[0].hour == 23
    assert spec[0].minute == 1
    assert spec[0].second == 16
    assert spec[0].file_format == "acq"


def test_field_spectrum_read_bad_suffix(datadir):
    with pytest.raises(TypeError, match="must be h5 or acq"):
        io.FieldSpectrum(datadir / "observation.yaml")


def test_hickle_roundtrip(calio, tmpdir):
    hickle.dump(calio, tmpdir / "tmp-calio.h5")
    new = hickle.load(tmpdir / "tmp-calio.h5")

    assert new == calio
