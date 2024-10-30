use crate::error::DmapError;
use crate::formats::dmap::Record;
use crate::types::{DmapField, DmapType, Fields, Type};
use indexmap::IndexMap;
use lazy_static::lazy_static;
use std::convert::TryFrom;

static SCALAR_FIELDS: [(&str, Type); 37] = [
    ("radar.revision.major", Type::Char),
    ("radar.revision.minor", Type::Char),
    ("origin.code", Type::Char),
    ("origin.time", Type::String),
    ("origin.command", Type::String),
    ("cp", Type::Short),
    ("stid", Type::Short),
    ("time.yr", Type::Short),
    ("time.mo", Type::Short),
    ("time.dy", Type::Short),
    ("time.hr", Type::Short),
    ("time.mt", Type::Short),
    ("time.sc", Type::Short),
    ("time.us", Type::Int),
    ("nave", Type::Short),
    ("lagfr", Type::Short),
    ("smsep", Type::Short),
    ("noise.search", Type::Float),
    ("noise.mean", Type::Float),
    ("channel", Type::Short),
    ("bmnum", Type::Short),
    ("bmazm", Type::Float),
    ("scan", Type::Short),
    ("rxrise", Type::Short),
    ("intt.sc", Type::Short),
    ("intt.us", Type::Int),
    ("nrang", Type::Short),
    ("frang", Type::Short),
    ("rsep", Type::Short),
    ("xcf", Type::Short),
    ("tfreq", Type::Short),
    ("noise.sky", Type::Float),
    ("combf", Type::String),
    ("fitacf.revision.major", Type::Int),
    ("fitacf.revision.minor", Type::Int),
    ("snd.revision.major", Type::Short),
    ("snd.revision.minor", Type::Short),
];

static SCALAR_FIELDS_OPT: [(&str, Type); 0] = [];

static VECTOR_FIELDS: [(&str, Type); 0] = [];

static VECTOR_FIELDS_OPT: [(&str, Type); 10] = [
    ("slist", Type::Short),
    ("qflg", Type::Char),
    ("gflg", Type::Char),
    ("v", Type::Float),
    ("v_e", Type::Float),
    ("p_l", Type::Float),
    ("w_l", Type::Float),
    ("x_qflg", Type::Char),
    ("phi0", Type::Float),
    ("phi0_e", Type::Float),
];

static MATCHED_VECS: [[&str; 10]; 1] = [[
    "slist", "qflg", "gflg", "v", "v_e", "p_l", "w_l", "x_qflg", "phi0", "phi0_e",
]];

lazy_static! {
    static ref SND_FIELDS: Fields<'static> = Fields {
        all_fields: {
            let mut fields: Vec<&str> = vec![];
            fields.extend(SCALAR_FIELDS.clone().into_iter().map(|x| x.0));
            fields.extend(SCALAR_FIELDS_OPT.clone().into_iter().map(|x| x.0));
            fields.extend(VECTOR_FIELDS.clone().into_iter().map(|x| x.0));
            fields.extend(VECTOR_FIELDS_OPT.clone().into_iter().map(|x| x.0));
            fields
        },
        scalars_required: SCALAR_FIELDS.to_vec(),
        scalars_optional: SCALAR_FIELDS_OPT.to_vec(),
        vectors_required: VECTOR_FIELDS.to_vec(),
        vectors_optional: VECTOR_FIELDS_OPT.to_vec(),
        vector_dim_groups: MATCHED_VECS.to_vec().iter().map(|x| x.to_vec()).collect(),
    };
}

#[derive(Debug, PartialEq, Clone)]
pub struct SndRecord {
    pub data: IndexMap<String, DmapField>,
}

impl SndRecord {
    pub fn get(&self, key: &String) -> Option<&DmapField> {
        self.data.get(key)
    }
    pub fn keys(&self) -> Vec<&String> {
        self.data.keys().collect()
    }
}
impl Record<'_> for SndRecord {
    fn inner(self) -> IndexMap<String, DmapField> {
        self.data
    }

    fn new(fields: &mut IndexMap<String, DmapField>) -> Result<SndRecord, DmapError> {
        match Self::check_fields(fields, &SND_FIELDS) {
            Ok(_) => {}
            Err(e) => Err(e)?,
        }

        Ok(SndRecord {
            data: fields.to_owned(),
        })
    }
    fn to_bytes(&self) -> Result<Vec<u8>, DmapError> {
        let (num_scalars, num_vectors, mut data_bytes) =
            Self::data_to_bytes(&self.data, &SND_FIELDS)?;

        let mut bytes: Vec<u8> = vec![];
        bytes.extend((65537_i32).as_bytes()); // No idea why this is what it is, copied from backscatter
        bytes.extend((data_bytes.len() as i32 + 16).as_bytes()); // +16 for code, length, num_scalars, num_vectors
        bytes.extend(num_scalars.as_bytes());
        bytes.extend(num_vectors.as_bytes());
        bytes.append(&mut data_bytes); // consumes data_bytes
        Ok(bytes)
    }
}

impl TryFrom<&mut IndexMap<String, DmapField>> for SndRecord {
    type Error = DmapError;

    fn try_from(value: &mut IndexMap<String, DmapField>) -> Result<Self, Self::Error> {
        Self::coerce::<SndRecord>(value, &SND_FIELDS)
    }
}
