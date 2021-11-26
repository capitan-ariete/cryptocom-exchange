from .structs import Coin

AAVE = Coin("AAVE")
ADA = Coin("ADA")
AGLD = Coin("AGLD")
ALGO = Coin("ALGO")
ALICE = Coin("ALICE")
AMP = Coin("AMP")
ANKR = Coin("ANKR")
AR = Coin("AR")
ARPA = Coin("ARPA")
ATOM = Coin("ATOM")
AUDIO = Coin("AUDIO")
AVAX = Coin("AVAX")
AXS = Coin("AXS")
BADGER = Coin("BADGER")
BAL = Coin("BAL")
BAND = Coin("BAND")
BAT = Coin("BAT")
BCH = Coin("BCH")
BNT = Coin("BNT")
BOBA = Coin("BOBA")
BOSON = Coin("BOSON")
BRZ = Coin("BRZ")
BTC = Coin("BTC")
BUSD = Coin("BUSD")
C98 = Coin("C98")
CELR = Coin("CELR")
CHR = Coin("CHR")
CHZ = Coin("CHZ")
CKB = Coin("CKB")
COMP = Coin("COMP")
COTI = Coin("COTI")
CQT = Coin("CQT")
CRO = Coin("CRO")
CRV = Coin("CRV")
CSPR = Coin("CSPR")
CTSI = Coin("CTSI")
DAI = Coin("DAI")
DAR = Coin("DAR")
DERC = Coin("DERC")
DINO = Coin("DINO")
DOGE = Coin("DOGE")
DOT = Coin("DOT")
DYDX = Coin("DYDX")
EFI = Coin("EFI")
EGLD = Coin("EGLD")
ELON = Coin("ELON")
ENJ = Coin("ENJ")
ENS = Coin("ENS")
EOS = Coin("EOS")
EPS = Coin("EPS")
ETC = Coin("ETC")
ETH = Coin("ETH")
FARM = Coin("FARM")
FET = Coin("FET")
FIL = Coin("FIL")
FLOW = Coin("FLOW")
FORTH = Coin("FORTH")
FTM = Coin("FTM")
FXS = Coin("FXS")
GALA = Coin("GALA")
GHST = Coin("GHST")
GLM = Coin("GLM")
GRT = Coin("GRT")
GTC = Coin("GTC")
GUSD = Coin("GUSD")
HBAR = Coin("HBAR")
HNT = Coin("HNT")
HOT = Coin("HOT")
HUSD = Coin("HUSD")
ICP = Coin("ICP")
ICX = Coin("ICX")
ILV = Coin("ILV")
INJ = Coin("INJ")
IOTX = Coin("IOTX")
IQ = Coin("IQ")
JASMY = Coin("JASMY")
KAVA = Coin("KAVA")
KEEP = Coin("KEEP")
KLAY = Coin("KLAY")
KNC = Coin("KNC")
KSM = Coin("KSM")
LINK = Coin("LINK")
LPT = Coin("LPT")
LRC = Coin("LRC")
LTC = Coin("LTC")
LUNA = Coin("LUNA")
MANA = Coin("MANA")
MASK = Coin("MASK")
MATIC = Coin("MATIC")
MCO = Coin("MCO")
MIR = Coin("MIR")
MKR = Coin("MKR")
MLN = Coin("MLN")
MOVR = Coin("MOVR")
NANO = Coin("NANO")
NEAR = Coin("NEAR")
NEO = Coin("NEO")
NKN = Coin("NKN")
NU = Coin("NU")
OCEAN = Coin("OCEAN")
OGN = Coin("OGN")
OMG = Coin("OMG")
ONE = Coin("ONE")
ONEINCH = Coin("1INCH")
ONT = Coin("ONT")
PAXG = Coin("PAXG")
PENDLE = Coin("PENDLE")
PERP = Coin("PERP")
PLA = Coin("PLA")
POLY = Coin("POLY")
QI = Coin("QI")
QNT = Coin("QNT")
QTUM = Coin("QTUM")
QUICK = Coin("QUICK")
RAD = Coin("RAD")
RARI = Coin("RARI")
REN = Coin("REN")
REQ = Coin("REQ")
RGT = Coin("RGT")
RLC = Coin("RLC")
RLY = Coin("RLY")
RNDR = Coin("RNDR")
RSR = Coin("RSR")
RUNE = Coin("RUNE")
RVN = Coin("RVN")
SAND = Coin("SAND")
SC = Coin("SC")
SDN = Coin("SDN")
SGB = Coin("SGB")
SHIB = Coin("SHIB")
SKL = Coin("SKL")
SLP = Coin("SLP")
SNX = Coin("SNX")
SOL = Coin("SOL")
SRM = Coin("SRM")
STORJ = Coin("STORJ")
STX = Coin("STX")
SUSHI = Coin("SUSHI")
TFUEL = Coin("TFUEL")
THETA = Coin("THETA")
TRB = Coin("TRB")
TRIBE = Coin("TRIBE")
TRU = Coin("TRU")
TUSD = Coin("TUSD")
UMA = Coin("UMA")
UNI = Coin("UNI")
USDC = Coin("USDC")
USDP = Coin("USDP")
USDT = Coin("USDT")
VET = Coin("VET")
VTHO = Coin("VTHO")
VVS = Coin("VVS")
WAVE = Coin("WAVE")
WAVES = Coin("WAVES")
WAXP = Coin("WAXP")
WBTC = Coin("WBTC")
XLM = Coin("XLM")
XRP = Coin("XRP")
XTZ = Coin("XTZ")
XYO = Coin("XYO")
YFI = Coin("YFI")
YGG = Coin("YGG")
ZIL = Coin("ZIL")
ZRX = Coin("ZRX")


def all():
    return [
        value for name, value in globals().items()
        if isinstance(value, Coin)
    ]
