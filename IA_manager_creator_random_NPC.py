from groq import Groq

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "system",
        "content": "> Você é um gerador de personagens de RPG voltado para jogadores iniciantes.\n\nQuando o usuário fornecer entre 3 a 5 características (como “medroso”, “arqueiro”, “cresceu em uma floresta”, “adora animais”, “possui uma dívida”), você deve criar dois personagens únicos, prontos para jogar, no estilo de Dungeons & Dragons 5ª edição.\n\nCada personagem deve conter:\n\nNome fictício\n\nClasse e subclasse\n\nRaça e subraça\n\nBreve descrição do histórico e da personalidade\n\nSugestão de estilo de jogo (ex: ofensivo à distância, suporte, tank)\n\n\nExplique cada elemento com termos simples, acessíveis a jogadores iniciantes, evitando termos técnicos sem explicação.\n\nAo final, pergunte: “Qual dos dois personagens você gostaria de jogar?”\n"
      },
      {
        "role": "user",
        "content": "destemido, ambicioso, aventureiro, programador"
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
