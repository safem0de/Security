from lxml import etree

XML_PATH = "C:/Users/NaweeparbW/Downloads/federationmetadata.xml"

def print_error_lines(path, line_number, window=2):
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        start = max(0, line_number - window - 1)
        end = min(len(lines), line_number + window)
        print("\n🔍 XML Context:")
        for i in range(start, end):
            pointer = "👉 " if (i + 1) == line_number else "   "
            print(f"{pointer}Line {i+1}: {lines[i].strip()}")
    except Exception as e:
        print(f"❌ ไม่สามารถอ่านไฟล์เพื่อ debug ได้: {e}")

def read_certificates_from_adfs_metadata(xml_path):
    try:
        # โหลด XML
        tree = etree.parse(xml_path)
        root = tree.getroot()

        # Define namespaces
        namespaces = {
            'md': 'urn:oasis:names:tc:SAML:2.0:metadata',
            'ds': 'http://www.w3.org/2000/09/xmldsig#'
        }

        # ค้นหา KeyDescriptor ที่ใช้สำหรับ signing
        key_descriptors = root.findall(".//md:KeyDescriptor[@use='signing']", namespaces)
        print(f"\n✅ พบใบรับรอง signing ทั้งหมด: {len(key_descriptors)}\n")

        # แสดง X509Certificate
        for idx, key in enumerate(key_descriptors, start=1):
            cert_elem = key.find(".//ds:X509Certificate", namespaces)
            if cert_elem is not None:
                print(f"📦 Key {idx}:")
                print(cert_elem.text.strip())
                print("-" * 80)
            else:
                print(f"⚠️ Key {idx} ไม่มี <ds:X509Certificate>")

    except etree.XMLSyntaxError as e:
        print(f"❌ XMLSyntaxError: {e}")
        print_error_lines(xml_path, e.lineno)
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    read_certificates_from_adfs_metadata(XML_PATH)
