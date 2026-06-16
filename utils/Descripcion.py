# prompt: Cargar archivo de excel
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import statsmodels.api as sm
import statsmodels.formula.api as r i, cat in enumerate(self.encoded_df.columns):
                        for j, cat2 in enumerate(self.encoded_df.columns):
                                        if i != j:
                                                            a = self.encoded_df[cat] / self.encoded_df[cat].sum()
                                                                                b = self.encoded_df[cat2] / self.encoded_df[cat2].sum()
                                                                                                    entre = (a - b) ** 2
                                                                                                                        dist = self.num_individuals * np.sum(entre)
                                                                                                                                            dist_df.loc[cat, cat2] = dist
                                                                                                                                                    return dist_df



                                                                                                                                                        def embedding(self, **kwargs):
                                                                                                                                                                    for elemento in kwargs:
                                                                                                                                                                                    le = LabelEncoder()
                                                                                                                                                                                                    self.df[f'id_unico_{elemento}'] = le.fit_transform(self.df[elemento])

                                                                                                                                                                                                                    min_val = self.df[f'id_unico_{elemento}'].min()
                                                                                                                                                                                                                                    max_val = self.df[f'id_unico_{elemento}'].max()
                                                                                                                                                                                                                                                    print(f"Son de {min_val} a {max_val}")

                                                                                                                                                                                                                                                                    if max_val >= 100:
                                                                                                                                                                                                                                                                                        embedding_valor = round(max_val / 100)
                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                            embedding_valor = round(max_val ** 0.5)

                                                                                                                                                                                                                                                                                                                                            tensor = nn.Embedding(num_embeddings=max_val + 1, embedding_dim=embedding_valor)

                                                                                                                                                                                                                                                                                                                                                            indices = torch.tensor(self.df[f'id_unico_{elemento                                                                                                                                                                                                              