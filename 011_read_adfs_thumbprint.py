import base64
import hashlib
from lxml import etree

XML_PATH = "C:/Users/NaweeparbW/Downloads/federationmetadata.xml"
# XML_PATH = "sp.xml"

def calc_thumbprints(cert_b64):
    """แปลง Base64 → DER และคำนวณ SHA-1 / SHA-256"""
    try:
        cert_der = base64.b64decode(cert_b64)
        sha1 = hashlib.sha1(cert_der).hexdigest().upper()
        sha256 = hashlib.sha256(cert_der).hexdigest().upper()
        return sha1, sha256
    except Exception as e:
        return None, None

def read_cert_and_thumbprint(xml_path):
    try:
        tree = etree.parse(xml_path)
        root = tree.getroot()

        namespaces = {
            'md': 'urn:oasis:names:tc:SAML:2.0:metadata',
            'ds': 'http://www.w3.org/2000/09/xmldsig#'
        }

        key_descriptors = root.findall(".//md:KeyDescriptor[@use='signing']", namespaces)
        print(f"\n✅ พบใบรับรอง signing ทั้งหมด: {len(key_descriptors)}\n")

        for idx, key in enumerate(key_descriptors, start=1):
            cert_elem = key.find(".//ds:X509Certificate", namespaces)
            if cert_elem is not None:
                cert_text = cert_elem.text.strip().replace("\n", "")
                sha1, sha256 = calc_thumbprints(cert_text)

                print(f"📦 Key {idx}")
                print(f"SHA-1 Thumbprint   : {sha1}")
                print(f"SHA-256 Thumbprint : {sha256}")
                print("-" * 80)
            else:
                print(f"⚠️ Key {idx} ไม่มี <ds:X509Certificate>")

    except etree.XMLSyntaxError as e:
        print(f"❌ XMLSyntaxError: {e}")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    read_cert_and_thumbprint(XML_PATH)
