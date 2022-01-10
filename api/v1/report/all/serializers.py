from rest_framework import serializers

from api.base.serializers import InheritedSerializer
from config.settings import DATETIME_INPUT_OUTPUT_FORMAT

class ChartResponseSerializer(InheritedSerializer):
    CHITIEU = serializers.CharField(help_text="`CHITIEU` of data")
    SODU_DS_LK_KYT = serializers.FloatField(help_text="`SODU_DS_LK_KYT` of data")
    THUC_HIEN_KY_T = serializers.FloatField(help_text="`THUC_HIEN_KY_T` of data")
    KE_HOACH_KY_T = serializers.FloatField(help_text="`KE_HOACH_KY_T` of data")
    TYLE_KY_T = serializers.FloatField(help_text="`TYLE_KY_T` of data")
    THUC_HIEN_LK = serializers.FloatField(help_text="`THUC_HIEN_LK` of data")
    KE_HOACH_LK = serializers.FloatField(help_text="`KE_HOACH_LK` of data")
    TY_LY_LK = serializers.FloatField(help_text="`TY_LY_LK` of data")
    DIEM_CHI_TIEU_LK = serializers.FloatField(help_text="`DIEM_CHI_TIEU_LK` of data")
    DIEM_KH_LK = serializers.FloatField(help_text="`DIEM_KH_LK` of data")
    KH_NAM = serializers.FloatField(help_text="`KH_NAM` of data")
    TY_LE_NAM = serializers.FloatField(help_text="`TY_LE_NAM` of data")
    DIEM_CHI_TIEU_KH_NAM = serializers.CharField(help_text="`DIEM_CHI_TIEU_KH_NAM` of data")
    DIEM_KH_NAM = serializers.CharField(help_text="`DIEM_KH_NAM` of data")
    AMOUNT_CHART = serializers.FloatField(help_text="`AMOUNT_CHART` of data")

class PFSChartResponseSerializer(InheritedSerializer):
    REGION_ID = serializers.IntegerField(help_text="`REGION_ID` of data")
    REGION_NAME = serializers.CharField(help_text="`REGION_NAME` of data")
    TY_LE_HTKH_LUY_KE_TANG_TRUONG_HDBQ_CKH = serializers.CharField(help_text="`TY_LE_HTKH_LUY_KE_TANG_TRUONG_HDBQ_CKH` of data")
    DIEM_HTKH_LUY_KE_TANG_TRUONG_HDBQ_CKH = serializers.FloatField(help_text="`DIEM_HTKH_LUY_KE_TANG_TRUONG_HDBQ_CKH` of data")
    TY_LE_HTKH_LUY_KE_TANG_TRUONG_HDBQ_KKH = serializers.CharField(help_text="`TY_LE_HTKH_LUY_KE_TANG_TRUONG_HDBQ_KKH` of data")
    DIEM_HTKH_LUY_KE_TANG_TRUONG_HDBQ_KKH = serializers.FloatField(help_text="`DIEM_HTKH_LUY_KE_TANG_TRUONG_HDBQ_KKH` of data")
    TY_LE_HTKH_DSGN = serializers.CharField(help_text="`TY_LE_HTKH_DSGN` of data")
    DIEM_HTKH_DSGN = serializers.FloatField(help_text="`DIEM_HTKH_DSGN` of data")
    TY_LE_HTKH_TPDV = serializers.CharField(help_text="`TY_LE_HTKH_TPDV` of data")
    DIEM_HTKH_TPDV = serializers.FloatField(help_text="`DIEM_HTKH_TPDV` of data")
    TY_LE_LNTT = serializers.CharField(help_text="`TY_LE_LNTT` of data")
    DIEM_LNTT = serializers.FloatField(help_text="`DIEM_LNTT` of data")
    TY_LE_BHNT = serializers.CharField(help_text="`TY_LE_BHNT` of data")
    DIEM_BHNT = serializers.FloatField(help_text="`DIEM_BHNT` of data")
    TY_LE_TDQT_MOI = serializers.CharField(help_text="`TY_LE_TDQT_MOI` of data")
    DIEM_TDQT_MOI = serializers.FloatField(help_text="`DIEM_TDQT_MOI` of data")
    TY_LE_TPBQ = serializers.CharField(help_text="`TY_LE_TPBQ` of data")
    DIEM_TPBQ = serializers.FloatField(help_text="`DIEM_TPBQ` of data")
    TY_LE_PHAT_TRIEN_KH_MOI = serializers.CharField(help_text="`TY_LE_PHAT_TRIEN_KH_MOI` of data")
    DIEM_PHAT_TRIEN_KH_MOI = serializers.FloatField(help_text="`DIEM_PHAT_TRIEN_KH_MOI` of data")

class EnterpriseChartResponseSerializer(InheritedSerializer):
    STT = serializers.IntegerField(help_text="`STT` of data")
    MONTH_ID = serializers.CharField(help_text="`MONTH_ID` of data")
    BRANCH_ID = serializers.CharField(help_text="`BRANCH_ID` of data")
    BRANCH_NAME = serializers.CharField(help_text="`BRANCH_NAME` of data")
    SORT_REGION = serializers.CharField(help_text="`SORT_REGION` of data")
    HE_SO_DIEM_THEO_MO_HINH_DVKD = serializers.CharField(help_text="`HE_SO_DIEM_THEO_MO_HINH_DVKD` of data")
    HTKH_LK_TANG_TRUONG_HD = serializers.FloatField(help_text="`HTKH_LK_TANG_TRUONG_HD` of data")
    DIEM_TANG_TRUONG_HD = serializers.FloatField(help_text="`DIEM_TANG_TRUONG_HD` of data")
    DIEM_TANG_TRUONG_HDVON_BQ_KKH = serializers.FloatField(help_text="`DIEM_TANG_TRUONG_HDVON_BQ_KKH` of data")
    HTKH_LK_TANG_TRUONG_CHOVAY = serializers.FloatField(help_text="`HTKH_LK_TANG_TRUONG_CHOVAY` of data")
    DIEM_TANG_TRUONG_CHOVAY = serializers.FloatField(help_text="`DIEM_TANG_TRUONG_CHOVAY` of data")
    HTKH_LK_TANG_TRUONG_CHOVAY_BQ = serializers.FloatField(help_text="`HTKH_LK_TANG_TRUONG_CHOVAY_BQ` of data")

    DIEM_TANG_TRUONG_CHOVAY_BQ = serializers.FloatField(help_text="`DIEM_TANG_TRUONG_CHOVAY_BQ` of data")
    HTKH_LK_THU_PHI_DICH_VU = serializers.FloatField(help_text="`HTKH_LK_THU_PHI_DICH_VU` of data")
    DIEM_THU_PHI_DICH_VU = serializers.FloatField(help_text="`DIEM_THU_PHI_DICH_VU` of data")
    HTKH_LK_THUPHI_TTQT_LNKDNH = serializers.FloatField(help_text="`HTKH_LK_THUPHI_TTQT_LNKDNH` of data")
    DIEM_THUPHI_TTQT_LNKDNH = serializers.FloatField(help_text="`DIEM_THUPHI_TTQT_LNKDNH` of data")
    HTKH_LK_DOANHSO_THANHTOAN_QR = serializers.FloatField(help_text="`HTKH_LK_DOANHSO_THANHTOAN_QR` of data")
    DIEM_DOANHSO_THANHTOAN_QR = serializers.FloatField(help_text="`DIEM_DOANHSO_THANHTOAN_QR` of data")
    HTKH_LK_MERCHANT_QR = serializers.FloatField(help_text="`HTKH_LK_MERCHANT_QR` of data")
    DIEM_MERCHANT_QR = serializers.FloatField(help_text="`DIEM_MERCHANT_QR` of data")

    HTKH_LK_DOANHSO_THANHTOAN_POS = serializers.FloatField(help_text="`HTKH_LK_DOANHSO_THANHTOAN_POS` of data")
    DIEM_DOANHSO_THANHTOAN_POS = serializers.FloatField(help_text="`DIEM_DOANHSO_THANHTOAN_POS` of data")
    HTKH_LK_LOI_NHUAN_TRUOC_THUE = serializers.FloatField(help_text="`HTKH_LK_LOI_NHUAN_TRUOC_THUE` of data")
    DIEM_LOI_NHUAN_TRUOC_THUE = serializers.FloatField(help_text="`DIEM_LOI_NHUAN_TRUOC_THUE` of data")
    HTKH_LK_SLKH_MOI = serializers.FloatField(help_text="`HTKH_LK_SLKH_MOI` of data")
    DIEM_SLKH_MOI = serializers.FloatField(help_text="`DIEM_SLKH_MOI` of data")

    HTKH_LK_SLHD_EBANKING = serializers.FloatField(help_text="`HTKH_LK_SLHD_EBANKING` of data")
    DIEM_SLHD_EBANKING = serializers.FloatField(help_text="`DIEM_SLHD_EBANKING` of data")
    HTKH_LK_KHMOI_SPVAYTIEN = serializers.FloatField(help_text="`HTKH_LK_KHMOI_SPVAYTIEN` of data")
    DIEM_KHMOI_SPVAYTIEN = serializers.FloatField(help_text="`DIEM_KHMOI_SPVAYTIEN` of data")
    HTKH_LK_DOANHSO_BAOLANH = serializers.FloatField(help_text="`HTKH_LK_DOANHSO_BAOLANH` of data")
    DIEM_DOANHSO_BAOLANH = serializers.FloatField(help_text="`DIEM_DOANHSO_BAOLANH` of data")

    DIEM_CHITIEU_CHATLUONG_DICHVU = serializers.FloatField(help_text="`DIEM_CHITIEU_CHATLUONG_DICHVU` of data")
    DIEM_CHITIEU_QLRR = serializers.FloatField(help_text="`DIEM_CHITIEU_QLRR` of data")
    DIEM_CBNV_NGHI_VIEC = serializers.FloatField(help_text="`DIEM_CBNV_NGHI_VIEC` of data")
    DIEM_TYLE_NO2_PHATSINH = serializers.FloatField(help_text="`DIEM_TYLE_NO2_PHATSINH` of data")
    DIEM_TYLE_NOXAU_PHATSINH = serializers.FloatField(help_text="`DIEM_TYLE_NOXAU_PHATSINH` of data")

    HTKH_LK_XULY_NOXAU_THONGTHUONG = serializers.FloatField(help_text="`HTKH_LK_XULY_NOXAU_THONGTHUONG` of data")
    DIEM_XULY_NOXAU_THONGTHUONG = serializers.FloatField(help_text="`DIEM_XULY_NOXAU_THONGTHUONG` of data")

    DIEM_KHUYEN_KHICH = serializers.FloatField(help_text="`DIEM_KHUYEN_KHICH` of data")
    TONG_DIEM = serializers.FloatField(help_text="`TONG_DIEM` of data")
    DIEU_CHINHG_TONG_DIEM = serializers.FloatField(help_text="`DIEU_CHINHG_TONG_DIEM` of data")
    TONG_DIEM_SAU_DIEU_CHINH = serializers.FloatField(help_text="`TONG_DIEM_SAU_DIEU_CHINH` of data")
    XEP_HANG = serializers.FloatField(help_text="`XEP_HANG` of data")
    XEP_LOAI = serializers.CharField(help_text="`XEP_LOAI` of data")
    STATUS = serializers.CharField(help_text="`STATUS` of data")
    PROCESS_DATE = serializers.CharField(help_text="`PROCESS_DATE` of data")




