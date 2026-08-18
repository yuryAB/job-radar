"""Configuração do radar pessoal de vagas iOS do Yury.

O perfil original de Dados/BI continua disponível no projeto. Esta configuração
é um perfil separado para manter a lógica compartilhada do JobRadar sem misturar
palavras-chave de áreas diferentes.
"""

from core.config import (
    DIGEST_HORA_UTC,
    INTERVALO_MINUTOS,
    LIMIAR_DIGEST_IMEDIATO,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    DB_PATH,
)

# Títulos inequívocos de desenvolvimento para Apple/mobile.
KEYWORDS_IOS_CARGO_FORTE = [
    "Desenvolvedor iOS",
    "Desenvolvedor Mobile",
    "Desenvolvedor Swift",
    "iOS Developer",
    "iOS Engineer",
    "Mobile Developer",
    "Mobile Engineer",
    "Swift Developer",
    "Swift Engineer",
    "Apple Developer",
    "Desenvolvedor de Aplicativos",
    "Aplicativos iOS",
]

# Títulos que podem ser de outras áreas; exigem tecnologia mobile/iOS no título.
KEYWORDS_IOS_CARGO_AMBIGUO = [
    "Software Engineer",
    "Software Developer",
    "Application Developer",
    "Engenheiro de Software",
    "Desenvolvedor de Software",
    "Frontend Developer",
    "Frontend Engineer",
]

QUALIFICADORES_IOS = [
    "ios",
    "swift",
    "swiftui",
    "uikit",
    "objective-c",
    "objective c",
    "apple",
    "mobile",
    "iphone",
    "ipad",
    "tvos",
    "watchos",
]

FERRAMENTAS_IOS_TITULO = [
    "Swift",
    "SwiftUI",
    "UIKit",
    "Objective-C",
    "iOS",
]

QUALIFICADORES_CARGO_IOS = [
    "developer",
    "desenvolvedor",
    "engineer",
    "engenheiro",
    "programador",
    "programmer",
    "especialista",
]

KEYWORDS_IOS = KEYWORDS_IOS_CARGO_FORTE + KEYWORDS_IOS_CARGO_AMBIGUO

TERMOS_CARGO_IOS = sorted({k.lower() for k in KEYWORDS_IOS})
TERMOS_FERRAMENTA_IOS = [
    "swift",
    "swiftui",
    "uikit",
    "objective-c",
    "xcode",
    "combine",
    "webrtc",
    "firebase",
    "fastlane",
    "ios",
    "mobile",
    "mvvm",
]
TERMOS_BUSCA_IOS = TERMOS_CARGO_IOS + TERMOS_FERRAMENTA_IOS
TERMOS_POR_CICLO_IOS = 12

# Presencial/híbrido apenas nas cidades aceitas; remoto vale para todo o Brasil.
# A ordem também prioriza as buscas de Manaus e Recife antes do Rio.
CIDADES_IOS = [
    "Remoto",
    "Manaus",
    "Recife",
    "Rio de Janeiro",
]

LOCATIONS_LINKEDIN_IOS = ["Brasil"]
LOCATIONS_LINKEDIN_REMOTO_APENAS_IOS = []
LOCATIONS_LINKEDIN_CIDADES_PRESENCIAL_IOS = [
    "Manaus",
    "Recife",
    "Rio de Janeiro",
]

# Vaga remota sem escopo explícito continua aceita; quando houver escopo,
# Brasil/LATAM são os mercados compatíveis com o perfil nacional.
MERCADOS_REMOTO_ACEITOS_IOS = ["Brasil", "LATAM"]

